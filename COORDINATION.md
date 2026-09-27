# Coordination note for Global Changes Orchestrator and the other sessions

**From:** Cloud agent researcher (cloud session).
**Updated:** 26 September 2026.

This cloud session can't send messages to other sessions, so this file is how it hands over. To reply, message Eric or append below.

## Status

| Item | State |
|---|---|
| Deceased estates and enforcement report | Done, verified against primary sources: `reports/2026-09-26_deceased-estates-and-enforcement.md` |
| Address history, logbooks and exits report (includes OS GB Address / AddressBase end of life in autumn 2027) | Done: `reports/2026-09-26_address-history-logbooks-exits.md` |
| Insights and 20 follow-up questions for other sessions | Done: `reports/2026-09-26_insights-and-follow-ups.md` |
| Empty-homes finder programme (A, A0, A00, A000, B–G), requested by "YouTube transcript mining" | Done (A–G): `reports/2026-09-26_empty-homes-finder.md` |

`main` now exists; all work is on `research/wiki-citations`, with a pull request into `main`.

## Headline findings (empty-homes finder)

1. **Gazette deceased-estates feed:** the best free per-address source.
   - A free Atom feed that needs no key.
   - Each notice gives the deceased's address, postcode, map point and date of death.
   - About 39k notices a year.
   - OGL licence, but it excludes personal data.
   - Fair use: 5 requests per 10 seconds, crawling 9pm–7am only.
2. **Class F exemptions (owner has died), MHCLG Council Taxbase 2025:** 124,064 dwellings in England.
   - The peak was 135.7k in 2023.
   - Top councils by count: Birmingham, Cornwall, North Yorkshire.
   - Top councils per 1,000 dwellings: Adur, Rother, Worthing.
3. **Long-term empties:** 303,185 (October 2025), of which 152,928 pay the premium.
   - No council openly publishes a per-address list of empty homes.
   - The government's compulsory purchase register lists 182 CPOs on individual houses since 2019, with addresses.
4. **FixMyStreet, North Lincolnshire:** only 53 reports in 2012, so validation against the 753 empties will be underpowered.
5. **Probate search:** a copy costs £16, not £1.50. The free search shows no address.

## ⚠ Do not use

**Do not build anything on the probate search service (probatesearch.service.gov.uk) beyond what its public web page displays, and do not probe it.**
- It appears to expose more data than intended.
- Eric has been briefed and is deciding on responsible disclosure.

## Asks for the orchestrator

- Where should results be routed, if not here?
- Does any running work (LiDAR, VOA builds, postcode scans) overlap with sections A–G? If so, say so and we'll avoid duplicating it.

---

## Division of labour, agreed 27 September 2026

After coordination with the "Empty Homes Search" session:

- **Empty Homes Search owns all per-address work:** ranked stuck-probate lists
  (Gazette + full Price Paid via transaction→UPRN links), the map, the valuation,
  and the per-address database. Eleven councils done (Wokingham, Bracknell Forest,
  Reading, Surrey Heath, Windsor & Maidenhead, Hart, Rushmoor, Slough, Runnymede,
  Woking, North Lincolnshire), Guildford in progress, ~290-council queue running.
  Output is local-only (Postgres + private map), not in any repo, by design
  (holds deceased addresses). **This cloud session does not build a parallel
  Gazette ranker or touch per-address data.** Task 2 stood down.
- **F3** (executor refunds gap) is their open task **OT-108** — left to them.
- **This cloud session owns external desk research:** F1 (legal), F2, F4, F9,
  F10 (national), F11, F12. Delivered in `reports/2026-09-27_followups-external.md`
  and `reports/2026-09-27_fca-perimeter-solicitor-brief.md`.
- **Knowledge base** is local-only (`0 - Operations/reference/kb/`, 558 entries),
  not on GitHub, so this cloud session cannot read it; paste entries as needed.
- **OS GB Address vs product comparison:** still waiting on a product description
  from a session/Eric before it can be done.

---

## Decisions and hand-offs, 27 September 2026 (later)

Settled between Eric, the Empty Homes Search session, and this cloud session.

**Care homes / Class E (recorded as an insight).** When an owner moves into care and
keeps the house, the death notice usually carries the *care home's* address; the house
returns via the "formerly of" line. The map v30 fix (commit `b4478462`) removes the
care home itself (CQC register match; numbered street addresses now need an exact
property-reference match to avoid catching ordinary houses that share a word with a
care-home name). Off the lists: Summerfield (Kidmore Road — was on the both-gone stuck
list), Bickerton House, Downshire House, Firfield House, Rivermede Court. **Insight:**
such a house is often empty since the *move into care* (Class E council-tax exemption),
not just since death — so "empty duration" for these can predate the death notice.
Gap: notices that give only the care home and never name the house leave it invisible.

**Title checks — Empty Homes Search owns; payment is Eric's.** Batch is **15 stuck
both-gone homes ≈ £105** (£7/title; no £3 option post-Dec-2024). List written locally to
`10 - empties/training/title_check_batch_2026-09-27.csv` (not committed — holds
addresses). Eric buys the **full register** on gov.uk "Search the register"; drops
owner/registration-date/price back for reading. Rule: read the stuck-vs-inherited hit
rate first (child + recent date + no price = inherited; deceased/executor/old date =
stuck), *then* decide if routine paid checks are worth it. This cloud session does not
touch per-address title data.

**Auction catalogues — parked** (unconfirmed lead + would require scraping).

**FixMyStreet — research done; the 2010–13 test IS feasible on free, no-scrape data.**
Verified against the *live* API (not just docs). Full note:
`scratchpad/notes/fixmystreet_open311_research.md`.
- **One national endpoint covers all GB councils** — no per-council list needed:
  `https://www.fixmystreet.com/open311/v2/requests.json?jurisdiction_id=fixmystreet`
  (`services.json` for categories). No API key for reads.
- **Historical depth (the make-or-break): cleared.** The generic Open311 "90-day cap"
  is documented but **not enforced** on this endpoint — a full-year 2012 span was
  accepted, and 2010 and 2012 reports came back live. The only real limit is **1000
  records/query, newest-first**, so page with rolling `start_date`/`end_date` windows.
  No HTML scraping at any step. mySociety retains *all* reports (FAQ) and they've been
  used in academic research before.
- **Categories** vary per council (2,572 today). Relevant strings: "Grass - Overgrown",
  "Abandoned Vehicle(s)", "Fly tipping", "Graffiti…", "Building Damage", and notably
  **"Estate Agent board…"**. No dedicated "empty/derelict building" national category —
  dereliction shows up indirectly. **2010–13 used simpler codes**, so classify on the
  strings in the *returned historical records*, not today's list.
- **Two cautions before building:** (1) **statistical power** — low-activity councils are
  too sparse (North Lincs had only 53 reports in all of 2012); run the test on a
  high-volume area (London boroughs / Oxfordshire / Bristol all appeared in 2010–13
  results). (2) **licensing** — report-data reuse has no stated open licence (software is
  AGPL); confirm reuse terms with mySociety before *publishing* anything derived from it.
- **So:** if the local test (2012 known-empties vs neighbour report-density) passes on a
  high-volume area, build the client once, locally. Endpoint + method are proven free.

**Gazette disclaimer notices — worth adding to the finder's source list.** When a
dissolved company owned a house, the property vests in the Crown as bona vacantia; if
the Crown disclaims it, the disclaimer notice **names the property**. This confirms
homes on the *company-limbo* list, free.
- **Notice-type code 2603** — "Notice of disclaimer", Companies Act 2006 **s.1013**
  (Crown/Treasury Solicitor disclaimer of property vesting as bona vacantia on
  company dissolution).
- Feed (Atom): `https://www.thegazette.co.uk/all-notices/notice/data.feed?noticetypes=2603`
  (or `...?text=disclaimer` as a looser fallback). Same feed mechanics as the
  deceased-estates feed (code 2903) the finder already uses.
- Scope note: this is *dissolved-company* onerous property, **not** deceased-estate BV
  houses (those are sold at auction, not disclaimed). A separate liquidator's disclaimer
  under Insolvency Act 1986 s.178 exists for property given up during a live liquidation.
