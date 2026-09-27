# Council-tax premium pressure — every English billing authority, scored

**Date:** 27 September 2026
**Data:** `data/premium_pressure_2025.csv` (296 authorities, one row each).
**Built from (both read/parsed directly this run, OGL v3.0):**
- MHCLG **Council Taxbase 2025 in England**, "Empty Properties Data" & "Second Homes Data" sheets — premium adoption + dwelling counts by duration tier. https://www.gov.uk/government/statistics/council-taxbase-2025-in-england
- MHCLG **Council Tax levels 2025-26**, Table 9 (area Band D, i.e. the full bill incl. county/police/fire/parish precepts — the correct base for the premium).

## What "premium pressure" means here
The empty-homes premium is a *motivation* signal: the more a stuck empty home costs its owner each year, and the sooner it starts, the more motivated the owner is to sell or act. The **bite_score (0–100)** proxies that, per council:
- **£ magnitude** (≤55 pts) — scaled area Band D. Premium rates are statutory and near-uniform, so the £ size of the bite is driven by the council tax level.
- **Trigger earliness** (≤30) — charges on 1–2yr-empty homes (**1-year trigger**) = 30; unknown = 12; **2-year trigger** = 6.
- **Long-empty stock actively charged** (≤10) — dwellings in the 10yr+ tier (n_10plus>0) = 10; 5–10yr = 4.
- **Second-home premium adopted** (+5).

## What's reliable vs assumed (read before using the £ columns)
- **Reliable from the data:** premium adoption (5.09), the four duration-tier dwelling **totals**, and Band D.
- **Trigger** is *inferred*: **170 councils confirmed 1-year** (they have 1–2yr dwellings charged), **25 confirmed 2-year** (adopted, can complete the 1–2yr table, zero there), **96 "unknown"** — they told MHCLG they *can't identify* 1–2yr dwellings (fold them into 2–5yr), so a per-council page is still needed for those. This quantifies the caveat flagged in Brief 4.
- **The £ columns assume the statutory schedule** (+100% at 1–2yr and 2–5yr, +200% at 5–10yr, +300% at 10yr+). The CTB rate-split columns are essentially unpopulated, so a council that sets *less* than the statutory maximum can't be detected from data — treat `premium_yr*_gbp` as "statutory premium if charged at that tier", not a guarantee.
- The premium bites the current owner **only if the home is empty and billed as such** — a motivation proxy, not a certainty (the lane already models this).

## Distribution
291/296 charge the empty-homes premium; 211/296 the second-homes premium. Scores: **127 councils ≥80, 115 at 60–79, 54 under 60.** Median 76.
**Five councils charge NO empty-homes premium** (zero pressure): Amber Valley, Bolsover, Castle Point, Gravesham, Ribble Valley.

## Top 20 by bite score (per-home pressure)
| Score | Council | Band D | Trigger | Premium at 10yr+ | 10yr+ stock |
|---:|---|---:|---|---:|---:|
| 100 | Dorset | £2,630 | 1yr | £7,891 | 37 |
| 100 | Lewes | £2,627 | 1yr | £7,882 | 12 |
| 100 | Nottingham | £2,656 | 1yr | £7,969 | 59 |
| 100 | Wealden | £2,608 | 1yr | £7,825 | 16 |
| 99 | Bristol | £2,584 | 1yr | £7,752 | 34 |
| 99 | West Devon | £2,574 | 1yr | £7,723 | 2 |
| 97 | Liverpool | £2,546 | 1yr | £7,639 | 169 |
| 96 | Eastbourne | £2,532 | 1yr | £7,597 | 13 |
| 96 | Mid Devon | £2,521 | 1yr | £7,564 | 17 |
| 96 | Rushcliffe | £2,532 | 1yr | £7,594 | 16 |
| 95 | Teignbridge | £2,513 | 1yr | £7,538 | 13 |
| 94 | Isle of Wight | £2,493 | 1yr | £7,480 | 15 |
| 94 | Kingston upon Thames | £2,489 | 1yr | £7,468 | 18 |
| 94 | Reading | £2,487 | 1yr | £7,461 | 10 |
| 94 | South Hams | £2,492 | 1yr | £7,475 | 9 |
| 94 | Walsall | £2,498 | 1yr | £7,495 | 31 |
| 94 | Woking | £2,482 | 1yr | £7,446 | 5 |
| 93 | Croydon | £2,480 | 1yr | £7,441 | 38 |
| 93 | Northumberland | £2,465 | 1yr | £7,394 | 79 |
| 93 | Preston | £2,478 | 1yr | £7,434 | 25 |

## Two lenses: bite vs supply
Bite (above) is pressure on *one* home. **Supply** — the count of premium-charged dwellings — is how many motivated owners a council actually has. The best hunting grounds score high on *both*:

**Most 10yr+ (deepest-stuck) stock:** Newham 398, Birmingham 251, Sheffield 211, **Liverpool 169**, **North Yorkshire 158**, Wiltshire 155, Durham 140, Bradford 133, Manchester 118, Newcastle 110, **Sefton 103**, **Cumberland 100**.
**Most total premium-charged dwellings:** Birmingham 5,193, Leeds 2,875, Durham 2,334, Kirklees 2,227, North Yorkshire 2,225, Liverpool 2,223, Bradford 2,190, Cornwall 1,821.

**High bite + high supply (the sweet spot):** **Liverpool** (97, 169 deep-stuck, + its £5–20k grant), **North Yorkshire** (90), **Sheffield** (88), **Cornwall** (92; Lendology loan too), **Bradford** (81), **Sefton** (92), **Cumberland** (89), **Birmingham** (80; huge supply).

## The 13 rollout boroughs, scored
| Score | Borough | Band D | Trigger |
|---:|---|---:|---|
| 94 | Reading | £2,487 | 1yr |
| 94 | Woking | £2,482 | 1yr |
| 88 | Wokingham | £2,376 | 1yr |
| 83 | Runnymede | £2,380 | 1yr |
| 83 | Slough | £2,299 | 1yr |
| 76 | Bracknell Forest | £2,155 | 1yr |
| 75 | North Lincolnshire | £2,238 | 1yr |
| 75 | Surrey Heath | £2,468 | unknown (folds-in) |
| 73 | Guildford | £2,429 | unknown (folds-in) |
| 67 | Spelthorne | £2,413 | unknown (folds-in) |
| 54 | Hart | £2,285 | 2yr |
| 50 | Rushmoor | £2,213 | 2yr |
| 39 | Windsor & Maidenhead | £1,824 | unknown (folds-in) |

(Confirms Brief 3/4: Rushmoor & Hart are 2-year-trigger laggards; W&M's low Band D makes it the weakest of the 13 on premium pressure. Surrey Heath/Guildford/Spelthorne "unknown" = their 1–2yr trigger needs a council-page check.)

## How to use it with Brief 4 (finance) and resale value
Premium pressure is one layer. To rank where a deal actually pays, overlay:
1. **This score** (motivated-seller pressure) — `bite_score` + `total_premium_dwellings` for supply.
2. **Buyer-friendly finance** (Brief 4 §C) — Kent's 12 districts, Derby, Burnley score *mid-table* on premium (Band D ~£2,200–2,450) but add a finance layer the top-scorers lack. **Note: letting-to-council grants (Liverpool etc.) are a valid exit, not a dead deal — buy-refurb-let/refinance still profits; they just realise the uplift over a hold.**
3. **Resale value + candidate counts** — the lane's own data. This is decisive: a high-pressure, high-supply council with low resale (e.g. some northern authorities) can still fail on margin once fixed costs are covered, exactly as North Lincs (£160k median) showed.

The clean rollout re-order: process **high bite × high supply** councils first (Liverpool, North Yorkshire, Cornwall, Sheffield, Bradford, Sefton, Cumberland, Birmingham), then the finance-advantaged Kent/Derby/Burnley cluster, filtering throughout on the lane's resale medians.

## CSV columns (`data/premium_pressure_2025.csv`)
`ons, la, region, band_d, empty_premium(Y/N), trigger(1yr/2yr/unknown/n/a), premium_yr1_gbp, premium_yr2_gbp, premium_yr5_gbp, premium_yr10_gbp, n_1_2, n_2_5, n_5_10, n_10plus, total_premium_dwellings, second_home_premium(Y/N), second_homes_count, bite_score`. Sorted by bite_score. £ figures are the statutory schedule × area Band D; re-weight the score freely from the raw columns.
