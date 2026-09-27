# Gap resolutions — 27 September 2026 (later)

Closing the open items from the prompt pack, done by the cloud session's own web search (Perplexity credits were exhausted). Same rules: external reading only, sources tagged.

## A. Premium triggers — 16 of the top-17 priority councils confirmed

Read from each council's **own .gov.uk page** [verified: primary]. All 16 have a **1-year trigger** at the statutory **100% / 200% / 300%** premium (1yr / 5yr / 10yr). `data/premium_pressure_2025.csv` updated: `trigger` → `1yr`, `premium_yr1_gbp` set, bite scores recomputed.

| Council | ONS | New score | Effective | Source |
|---|---|---:|---|---|
| Rutland | E06000017 | 100 | 1 Apr 2025 | rutland.gov.uk council-tax-charges-empty-homes |
| Oxford | E07000178 | 98 | 1 Apr 2024 | oxford.gov.uk empty-property-premium |
| Rother | E07000064 | 98 | — | rother.gov.uk empty-properties |
| County Durham | E06000047 | 97 | 1 Apr 2024 | durham.gov.uk article/3458 |
| Hastings | E07000062 | 97 | 1 Apr 2024 | hastings.gov.uk empty-secondhomes |
| Gedling | E07000173 | 95 | 1 Apr 2024 | gedling.gov.uk empty-properties |
| North Devon | E07000043 | 95 | 1 Apr 2024 | northdevon.gov.uk charges-for-second-homes |
| Hartlepool | E06000001 | 94 | 1 Apr 2024/25 | hartlepool.gov.uk charges-empty-properties |
| Newark & Sherwood | E07000175 | 94 | 1 Apr 2024 | newark-sherwooddc.gov.uk emptyproperties |
| Surrey Heath | E07000214 | 93 | — | surreyheath.gov.uk homes-become-empty-pclc |
| Oldham | E08000004 | 92 | 1 Apr 2024 | oldham.gov.uk empty_properties |
| Leicester | E06000016 | 89 | — | leicester.gov.uk empty-properties |
| Ipswich | E07000202 | 87 | 1 Apr 2024 | ipswich.gov.uk property-exemptions |
| Mid Sussex | E07000228 | 87 | 1 Apr 2025 | midsussex.gov.uk empty-properties |
| Richmond upon Thames | E09000027 | 87 | 1 Apr 2025 | richmond.gov.uk long-term-empty-premium |
| Warwick | E07000222 | 87 | 1 Apr 2024 | warwickdc.gov.uk empty_properties |

**Gateshead (E08000037) — still `unclear`.** Council pages and moderngov PDFs are behind a Cloudflare JS challenge (403 to fetch and to browser-UA curl). A search-engine snippet of Gateshead's *own* page (article 27202) suggests a **2-year** trigger for 2025/26, with the 1-year reduction and second-homes premium starting **1 April 2026** — plausible but not confirmed from a directly-read page, so left `unclear`. Needs a manual browser read.

**Trigger counts now:** 186 confirmed 1yr · 80 unknown (fold-in) · 25 confirmed 2yr · 5 no premium. (Was 170/96/25/5.) The remaining 80 can be run the same way from the prompt pack.

## B. The six non-council dead-ends

1. **Bona vacantia auction lots** — Crown stock does sell at auction under the seller name *"Solicitor for the Affairs of His/Her Majesty's Treasury"* (Treasury Solicitor / GLD BVD); **Allsop** is the house most associated. gov.uk (BVC2) confirms BVD land is normally sold "at public auction". A specific past catalogue lot URL could **not** be confirmed (Allsop lots sit behind its search). [secondary; lot URL not found]
2. **VAT empty-period evidence case** — *G S Bhachu v HMRC* (FTT, ref TC/2012/07473): 5% claimed but none of the Notice-708 evidence (council tax / electoral roll / utilities / EPO letter) produced → appeal failed. Confirms the **EPO letter is the safe route**. [secondary; primary decision URL not found]. Note: *P N Bewley Ltd* [2019] UKFTT 65 is **SDLT, not VAT** (already cited correctly in Brief 4's derelict-shell section).
3. **ICO — reusing published data for marketing** — nearest analogue is the **ICO Enforcement Notice v Experian (27 Oct 2020)**: personal data for marketing sourced partly from open/published sources (Open Electoral Register, Companies House) with inadequate transparency; ICO rejected reliance on general public notices over direct notification (later partly overturned, FTT 2023 / UT 2024). **No ICO action specific to Gazette/probate-notice reuse.** [secondary + primary doc]
4. **LAHF per-council allocations** — **no single official per-council table** exists (confirmed on the gov.uk collection page). Totals: R1 £500m (182 LAs+GLA), R2 £250m, R3 £500m, R4 £950m. Per-council amounts only via individual council decision papers / PQs. [verified: primary for the absence]
5. **FixMyStreet report-data licence** — **no open licence** on the report data (software is AGPL). Research/coordinate data is available *by arrangement* from the mySociety research team; commercial/high-volume reuse requires contacting mySociety. Effective position: **bespoke / by-arrangement**. So the 2010–13 test is fine to *run*; *publishing* derived output needs mySociety's agreement. [verified: primary]
6. **Policy in Practice "Missing Out"** — latest is **2025** (Sept 2025): £24.1bn total unclaimed (GB), Council Tax Support £3.3bn (~7.5m households). **No 2026 edition published** as of today. So F12's 2025 figures remain current; re-check later. [verified: primary for 2025; 2026 not found]

## Still open
- **80 unknown-trigger councils** + **Gateshead** — run the prompt pack (`requests/perplexity_council_premium_prompts.md`) the same way.
- **Legal items** (buyer obtaining the EPO letter pre-purchase; executor-outreach lawfulness) — a solicitor's call, not desk-resolvable.
