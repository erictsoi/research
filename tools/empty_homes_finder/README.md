# Empty-homes finder — prototype

A minimal, free-sources-only pipeline that turns **The Gazette's Deceased
Estates notices** (Trustee Act 1925 s.27) into a ranked list of candidate
long-term-empty homes — the "stuck probate family home" lead.

This is a prototype to prove the pipeline, not a production system.

## Why this source

From the research (`reports/2026-09-26_empty-homes-finder.md`), the Gazette
deceased-estates feed is the best free per-address lead source:

- Free Atom feed, no key.
- Each notice carries the deceased's **address, postcode, map point and dates**.
- ~39,000 notices a year.

## What it does

1. **Fetch** recent Deceased Estates notices from the Gazette open feed
   (`noticetypes=2903`), rate-limited to the Gazette's fair-use rules.
2. **Parse** each notice into `name, address, postcode, lat/lon, published,
   claim_deadline`.
3. **Filter** out likely care-home / institutional addresses (a death there
   usually does not free a house the estate owns).
4. **Score** each remaining lead, transparently and additively, so a human can
   see *why* it ranked where it did.
5. **Output** a ranked CSV or JSON, with an option to redact names.

## Run it

```bash
# Offline test — no network, proves parse/filter/score
python3 finder.py --self-test

# Tiny live demo — one request, 5 notices, names redacted, preview to screen
python3 finder.py --sample 5 --redact-names

# A real window — last 30 days, polite paging, written to a file
python3 finder.py --days 30 --max-pages 5 --redact-names --out leads.csv

# Add the free "no recent sale" signal from HM Land Registry Price Paid Data
python3 finder.py --days 30 --max-pages 5 \
    --price-paid pp-complete.csv --out leads.csv
```

Python 3.8+, standard library only. No dependencies to install.

## Scoring signals (all free)

| Signal | Source | Effect |
|---|---|---|
| Has a usable postcode | the notice | needed to act at all |
| Age of the notice | the notice | older → more time to have stalled |
| No sale since the notice | HM Land Registry Price Paid Data (`--price-paid`, OGL, free) | strong "still unsold" signal; a later sale is scored **down** as likely resolved |
| EPC age / absence | reserved hook (`--epc`) | old or missing EPC hints at long vacancy |

Weights are deliberately simple. Tune them against real outcomes (e.g. the
North Lincolnshire 2012 labelled set) before trusting the ranking.

## Ideas to extend

- **Price Paid join** is wired; point `--price-paid` at the monthly
  `pp-complete.csv` (or a filtered county file) from GOV.UK.
- **EPC join**: load a local EPC extract and add "no EPC" / "EPC older than N
  years" to the score. The register is free (registration required); the UPRN
  is OGL, address fields are restricted to energy-efficiency use.
- **Council public-health funeral data**: ~26 councils publish this openly;
  Calderdale includes full street addresses. A second free address feed.
- **Compulsory purchase register** (GOV.UK): 182 empty-house CPOs since 2019,
  with addresses — a late-stage cross-check.
- **UPRN**: geocode addresses to OS Open UPRN so the leads join cleanly to
  other datasets.

## Rules this prototype follows

- **Free sources only.** No paid data, no FOI, no contacting anyone.
- **The probate search back end is off-limits.** It exposes more than its
  public page shows; do not use it. See the project handoff.
- **Personal data.** Notices name deceased people and their last address. The
  Gazette is Open Government Licence, but **the OGL excludes personal data**,
  so handle output under research / legitimate-interest terms: minimise, do
  not publish, and prefer `--redact-names` for anything shared. An empty home
  advertised as empty is a burglary target — consider delaying or suppressing.
- **Fair use.** At most 5 requests / 10 seconds, and the Gazette asks that
  crawling run 21:00–07:00. The script rate-limits itself and defaults to a
  tiny sample; do not remove the limiter to bulk-harvest.

## Do not commit lead output

`.gitignore` here excludes `*.csv` / `*.json` so real notice data (personal
data) never lands in the repo. Write outputs elsewhere.
