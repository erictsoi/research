#!/usr/bin/env python3
"""
Empty-homes finder — prototype pipeline (free public sources only).

WHAT THIS DOES
    Pulls recent "Deceased Estates" notices (Trustee Act 1925 s.27) from The
    Gazette's open data feed, extracts the property address, postcode, location
    and dates, drops likely care-home addresses, and scores each lead. The
    output is a ranked list of candidate long-term-empty homes (stuck probate
    family homes) for a human to review.

SCOPE AND LIMITS (read before using)
  - Free sources only. No paid data, no FOI, no contacting anyone. This
    prototype fetches only The Gazette open feed. Price-paid and EPC signals
    are wired as OPTIONAL local-file joins (see --price-paid / --epc); the
    finder never calls a paid API.
  - It does NOT use the probate search back end. That service exposes more
    than its public page shows and must not be used (see the project handoff).
  - Personal data. Gazette notices name deceased people and their last
    address. The Gazette is Open Government Licence, but the OGL excludes
    personal data, so this is processed under legitimate-interest / research
    terms, minimised, and NOT committed anywhere public. Use --redact-names
    for outputs you share. Consider delaying or suppressing results: an empty
    home advertised as such is a burglary target.
  - Fair use. The Gazette asks for at most 5 requests per 10 seconds and
    crawling only 21:00-07:00. This script rate-limits itself and defaults to
    a tiny sample. Do not remove the limiter to bulk-harvest.

USAGE
    python3 finder.py --sample 5                 # tiny demo, 1 request
    python3 finder.py --days 30 --max-pages 3    # last 30 days, polite paging
    python3 finder.py --sample 5 --redact-names --out leads.csv
    python3 finder.py --self-test                # offline test, no network

No third-party dependencies (Python 3.8+ standard library only).
"""
from __future__ import annotations

import argparse
import csv
import dataclasses
import datetime as dt
import html
import json
import re
import sys
import os
import ssl
import time
import urllib.parse
import urllib.request

FEED = "https://www.thegazette.co.uk/all-notices/notice/data.feed"
DECEASED_ESTATES = "2903"  # Gazette notice-type code for Deceased Estates
USER_AGENT = "empty-homes-finder-prototype/0.1 (research; polite; low-volume)"

# Care-home / institutional address markers. Word-boundary matched, case
# insensitive. Kept conservative to avoid dropping ordinary houses on, say,
# "Nursery Lane". Tune against a labelled set before relying on it.
CARE_HOME_TERMS = [
    r"care home", r"nursing home", r"residential home", r"care centre",
    r"care center", r"rest home", r"retirement (?:home|village|community)",
    r"nursing centre", r"convalescent", r"\bhospice\b", r"care facility",
    r"extra care", r"sheltered (?:housing|accommodation)",
]
CARE_HOME_RE = re.compile("|".join(CARE_HOME_TERMS), re.I)

# UK postcode (outward+inward), loose but serviceable.
POSTCODE_RE = re.compile(r"\b([A-Z]{1,2}\d[A-Z\d]?)\s*(\d[A-Z]{2})\b", re.I)


@dataclasses.dataclass
class Lead:
    notice_id: str = ""
    name: str = ""
    address: str = ""
    postcode: str = ""
    lat: str = ""
    lon: str = ""
    published: str = ""
    claim_deadline: str = ""
    care_home: bool = False
    score: float = 0.0
    reasons: str = ""
    link: str = ""


# ----------------------------------------------------------------------------
# Fetch
# ----------------------------------------------------------------------------
class RateLimiter:
    """At most `n` requests per `per` seconds (Gazette fair use = 5/10s)."""

    def __init__(self, n: int = 5, per: float = 10.0) -> None:
        self.n, self.per, self.calls = n, per, []

    def wait(self) -> None:
        now = time.monotonic()
        self.calls = [t for t in self.calls if now - t < self.per]
        if len(self.calls) >= self.n:
            time.sleep(self.per - (now - self.calls[0]) + 0.05)
        self.calls.append(time.monotonic())


def fetch_feed(page_size: int, page: int, start_date: str | None,
               limiter: RateLimiter) -> str:
    params = {"noticetypes": DECEASED_ESTATES,
              "results-page-size": str(page_size), "results-page": str(page)}
    if start_date:
        params["start-publish-date"] = start_date
    url = FEED + "?" + urllib.parse.urlencode(params)
    limiter.wait()
    # NB: the feed misbehaves on a specific Accept type; "*/*" is reliable.
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                               "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=30, context=_ssl_context()) as r:
        return r.read().decode("utf-8", "replace")


def _ssl_context() -> ssl.SSLContext:
    """Default trust store, plus a corporate/proxy CA bundle if one is present
    (harmless when absent, e.g. on a normal machine)."""
    ctx = ssl.create_default_context()
    for path in (os.environ.get("SSL_CERT_FILE"),
                 os.environ.get("REQUESTS_CA_BUNDLE"),
                 "/root/.ccr/ca-bundle.crt"):
        if path and os.path.exists(path):
            try:
                ctx.load_verify_locations(path)
            except ssl.SSLError:
                pass
    return ctx


# ----------------------------------------------------------------------------
# Parse (regex, to avoid namespace-aware XML boilerplate for a prototype)
# ----------------------------------------------------------------------------
def _tag(entry: str, tag: str) -> str:
    m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", entry, re.S)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""


def parse_entries(xml: str) -> list[Lead]:
    leads: list[Lead] = []
    for entry in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        lead = Lead()
        lead.name = html.unescape(_tag(entry, "title"))
        lead.notice_id = _tag(entry, "id").rsplit("/", 1)[-1]
        lead.published = _tag(entry, "published")[:10]
        lm = re.search(r'<link[^>]*href="([^"]+)"', entry)
        lead.link = lm.group(1) if lm else ""
        lead.lat = _tag(entry, "geo:lat")
        lead.lon = _tag(entry, "geo:long")

        content = re.search(r"<content[^>]*>(.*?)</content>", entry, re.S)
        inner = html.unescape(content.group(1)) if content else ""
        pairs = dict(zip(
            [re.sub(r"<[^>]+>", "", d).strip().lower()
             for d in re.findall(r"<dt>(.*?)</dt>", inner, re.S)],
            [re.sub(r"<[^>]+>", "", d).strip()
             for d in re.findall(r"<dd>(.*?)</dd>", inner, re.S)]))
        lead.address = pairs.get("address of deceased", "")
        lead.claim_deadline = pairs.get("date of claim deadline", "")

        pc = POSTCODE_RE.search(lead.address)
        lead.postcode = (pc.group(1) + " " + pc.group(2)).upper() if pc else ""
        lead.care_home = bool(CARE_HOME_RE.search(lead.address))
        leads.append(lead)
    return leads


# ----------------------------------------------------------------------------
# Optional free-data signals (local files; never a paid API)
# ----------------------------------------------------------------------------
def load_ppd_postcodes(path: str) -> dict[str, str]:
    """HM Land Registry Price Paid Data CSV -> {postcode: latest_sale_date}.
    PPD is free (OGL). Columns are positional; postcode is col 3, date col 2."""
    latest: dict[str, str] = {}
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        for row in csv.reader(f):
            if len(row) < 4:
                continue
            date, pc = row[2][:10], row[3].strip().upper()
            if pc and (pc not in latest or date > latest[pc]):
                latest[pc] = date
    return latest


# ----------------------------------------------------------------------------
# Score
# ----------------------------------------------------------------------------
def _years_since(date_str: str, today: dt.date) -> float | None:
    try:
        return (today - dt.date.fromisoformat(date_str[:10])).days / 365.25
    except (ValueError, TypeError):
        return None


def score_lead(lead: Lead, ppd: dict[str, str] | None, today: dt.date) -> None:
    """Higher score = more likely a stuck, still-unsold empty. Transparent and
    additive so a human can see why. Tune weights against real outcomes."""
    score, reasons = 0.0, []

    # 1. Has a usable address + postcode (needed to act on it at all).
    if lead.postcode:
        score += 1.0
        reasons.append("has postcode")

    # 2. Time since the estate notice: older notice, more time to have stalled.
    yrs = _years_since(lead.published, today)
    if yrs is not None and yrs >= 0.5:
        score += min(yrs, 3.0)  # cap contribution at 3
        reasons.append(f"notice {yrs:.1f}y old")

    # 3. No recorded sale since the notice (price-paid join, if provided).
    if ppd is not None and lead.postcode:
        last_sale = ppd.get(lead.postcode)
        if last_sale is None:
            score += 1.0
            reasons.append("no PPD sale in postcode")
        elif last_sale[:10] < lead.published:
            score += 1.5
            reasons.append(f"no sale since notice (last {last_sale[:10]})")
        else:
            score -= 2.0
            reasons.append(f"SOLD {last_sale[:10]} — likely resolved")

    # 4. EPC-age signal: hook left for a local EPC join (see README).

    lead.score = round(score, 2)
    lead.reasons = "; ".join(reasons)


# ----------------------------------------------------------------------------
# Pipeline
# ----------------------------------------------------------------------------
def run(args) -> list[Lead]:
    limiter = RateLimiter()
    start_date = None
    if args.days:
        start_date = (dt.date.today() - dt.timedelta(days=args.days)).isoformat()

    raw: list[Lead] = []
    if args.sample:
        raw = parse_entries(fetch_feed(args.sample, 1, start_date, limiter))
    else:
        for page in range(1, args.max_pages + 1):
            batch = parse_entries(fetch_feed(args.page_size, page, start_date,
                                             limiter))
            if not batch:
                break
            raw.extend(batch)

    ppd = load_ppd_postcodes(args.price_paid) if args.price_paid else None
    today = dt.date.today()
    kept = [l for l in raw if not l.care_home]
    for lead in kept:
        score_lead(lead, ppd, today)
    kept.sort(key=lambda l: l.score, reverse=True)

    dropped = len(raw) - len(kept)
    print(f"[finder] fetched {len(raw)} notices, dropped {dropped} care-home, "
          f"ranked {len(kept)} leads", file=sys.stderr)
    return kept


def write_output(leads: list[Lead], path: str | None, redact: bool) -> None:
    fields = [f.name for f in dataclasses.fields(Lead)]
    rows = []
    for l in leads:
        d = dataclasses.asdict(l)
        if redact:
            d["name"] = "[redacted]"
        rows.append(d)
    if path and path.endswith(".json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(rows, f, indent=2)
    elif path:
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
    else:  # stdout preview
        for r in rows[:20]:
            print(f"{r['score']:>5}  {r['postcode']:<9}  "
                  f"{'CARE ' if r['care_home'] else ''}{r['reasons']}")
    if path:
        print(f"[finder] wrote {len(rows)} leads to {path}", file=sys.stderr)


# ----------------------------------------------------------------------------
# Offline self-test (no network) — proves parse/filter/score without fetching.
# ----------------------------------------------------------------------------
SELFTEST_XML = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
 <entry><title>SMITH, Ada</title><id>tag:g,2024:notice/AAAA</id>
  <published>2024-02-01T00:00:00Z</published>
  <link href="https://www.thegazette.co.uk/notice/AAAA"/>
  <geo:lat>53.1</geo:lat><geo:long>-1.1</geo:long>
  <content type="html">&lt;dl&gt;&lt;dt&gt;Address of Deceased&lt;/dt&gt;
   &lt;dd&gt;12 Rowan Close, Exampleton, EX1 2YZ&lt;/dd&gt;
   &lt;dt&gt;Date of Claim Deadline&lt;/dt&gt;&lt;dd&gt;2024-05-01&lt;/dd&gt;&lt;/dl&gt;
  </content></entry>
 <entry><title>JONES, Bryn</title><id>tag:g,2024:notice/BBBB</id>
  <published>2026-08-01T00:00:00Z</published>
  <link href="https://www.thegazette.co.uk/notice/BBBB"/>
  <content type="html">&lt;dl&gt;&lt;dt&gt;Address of Deceased&lt;/dt&gt;
   &lt;dd&gt;Fern Nursing Home, Careville, CV3 4AB&lt;/dd&gt;
   &lt;dt&gt;Date of Claim Deadline&lt;/dt&gt;&lt;dd&gt;2026-11-01&lt;/dd&gt;&lt;/dl&gt;
  </content></entry>
</feed>"""


def self_test() -> int:
    leads = parse_entries(SELFTEST_XML)
    assert len(leads) == 2, "should parse two entries"
    ada = next(l for l in leads if l.notice_id == "AAAA")
    assert ada.postcode == "EX1 2YZ", ada.postcode
    assert ada.address.startswith("12 Rowan Close"), ada.address
    assert ada.care_home is False
    bryn = next(l for l in leads if l.notice_id == "BBBB")
    assert bryn.care_home is True, "nursing home should be flagged"
    kept = [l for l in leads if not l.care_home]
    assert len(kept) == 1
    for l in kept:
        score_lead(l, {"EX1 2YZ": "2015-06-01"}, dt.date(2026, 9, 26))
    assert ada.score > 0, ada.score
    assert "no sale since notice" in ada.reasons, ada.reasons
    print("self-test OK: parsed 2, dropped 1 care-home, scored 1 "
          f"(EX1 2YZ score={ada.score}, reasons: {ada.reasons})")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Empty-homes finder prototype "
                                            "(free sources only).")
    p.add_argument("--sample", type=int, metavar="N",
                   help="fetch a single page of N notices (tiny demo)")
    p.add_argument("--days", type=int, help="only notices published in the "
                                            "last N days")
    p.add_argument("--max-pages", type=int, default=1,
                   help="max pages when not using --sample")
    p.add_argument("--page-size", type=int, default=50)
    p.add_argument("--price-paid", metavar="CSV",
                   help="optional HM Land Registry Price Paid Data CSV to add "
                        "a 'no recent sale' signal")
    p.add_argument("--epc", metavar="CSV", help="reserved: local EPC extract")
    p.add_argument("--redact-names", action="store_true",
                   help="replace deceased names with [redacted] in output")
    p.add_argument("--out", metavar="PATH", help="write .csv or .json; "
                                                 "otherwise prints a preview")
    p.add_argument("--self-test", action="store_true",
                   help="run offline tests and exit (no network)")
    args = p.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.sample and not args.days:
        p.error("give --sample N for a demo, or --days N for a window")
    leads = run(args)
    write_output(leads, args.out, args.redact_names)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
