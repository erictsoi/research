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

There is no `main` branch yet, so no pull requests have been opened. Work is on `research/wiki-citations`.

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
