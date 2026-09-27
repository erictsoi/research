# Brief 4 — where an empty-home purchase pays (national incentive stacking)

**Date:** 27 September 2026
**For:** Empty Homes Search, via Eric. Extends Brief 3 item 7 from 13 councils toward all of England (+ Wales noted).
**Rules honoured:** external reading only. No FOIs, no contact, no paid data, no addresses.
**Tags:** [verified: primary] = source read + quoted this run; [secondary] = reputable roundup/news; [inferred] = reasoning shown. Every row from a secondary source is flagged.

## Method and its limit (read first)

A fully-[verified] row for each of the ~296 English billing authorities is **not achievable read-only** — most council pages are Cloudflare/bot-gated. So this is built **source-first**, which is both more honest and more useful:
- **Premium practice** → one national dataset gives it for all 296 (§A).
- **Loan finance** → most council empty-homes loans are run by **three regional CICs**, not the councils; mapping those covers the finance question in a few passes (§B).
- **Grants / investor-friendly money / other stacking** → §C–§F, largely from roundups, every row tagged.

**The headline correction to Brief 3:** the "council money for a **buyer**" layer is much thinner than Brief 3's tentative [secondary] rows implied. **Every council-partnered loan scheme readable this run finances an existing OWNER improving a home they already hold — none clearly finances the PURCHASE of an empty home by a new buyer-renovator.** And the scheme Brief 3 put Bracknell Forest in (FHIL) is **winding down** (see §B3). So Brief 3's Tier-1 "Bracknell/Woking/Guildford = buyer finance" is weaker than stated: Woking & Guildford are **Parity Trust owner-improvement** loans; Bracknell's route (FHIL) is closing. Treat the genuinely buyer-usable money as the short list in §C, not the regional-lender maps.

---

## §A. Long-term-empty premium, nationally — one dataset does it

**Best source: MHCLG "Council Taxbase 2025 in England", the Local Authority level workbook** (`2025_Local_Authority_Drop_Down.xlsx`, published 6 Nov 2025, rev. 21 Jan 2026 — parsed directly this run). [verified: primary] https://www.gov.uk/government/statistics/council-taxbase-2025-in-england

Per billing authority (all 296) it carries:
- An **"Empty Properties Data"** sheet (39 tables): Table 5.09 = has the empty-homes premium been applied 2025-26 (yes/no); then dwelling counts by **premium rate × duration tier × band** across all four statutory tiers (1–2yr, 2–5yr, 5–10yr, 10yr+), each with an explicit "additional percentage premium (%)" column.
- A **"Second Homes Data"** sheet (Table 6.06): adoption yes/no + counts at 50/100%.

**National counts computed from the workbook** [verified: primary]: **291 of 296** authorities apply the empty-homes premium; **211 of 296** apply the second-homes premium; 170/296 report >0 dwellings in the 1–2yr tier.

**Honest limit — the 1yr-vs-2yr trigger is NOT cleanly in the data.** There's no "trigger" field; you'd infer it from the 1–2yr tables, but **Table 5.11 shows 79 authorities fold their 1–2yr dwellings into the 2–5yr figure and 20 more can't identify them (~34%)** — so a zero in the 1–2yr tier does *not* prove a 2-year trigger (e.g. Kensington & Chelsea, City of London). For those, the trigger still needs the council's own resolution/charge page.

- The MHCLG **Council Tax levels** release does **not** carry premium data (Band D/precepts only) — confirmed. No independent per-council FOI aggregation found; other material (Empty Homes Network, Commons Library) is re-analysis of this same CTB data. [verified: primary / secondary]

**What this lets the lane do:** build a national per-council table of *empty-premium adoption, 5yr/10yr tiers and second-home adoption* straight from the CTB workbook — with the 1-year trigger as the one field still needing per-council confirmation for the ~34% who fold it in.

---

## §B. Regional revolving-loan CICs — the finance backbone (all owner-improvement)

| Provider | Status | Councils covered | Buyer *purchase* financed? | Terms / strings |
|---|---|---|---|---|
| **Lendology CIC** | **OPEN** | **20** (empty-property list, primary) | **No — owners only** [verified: primary] | From £1,000, ≤15yr, fixed ~4.2% APR (not interest-free), Title Restriction security, 6–24mo deferred option; no let-back/nomination strings found |
| **Parity Trust** | **OPEN** | **16** (logos, secondary) | **No** for the council loan (existing owner/leaseholder); its separate direct "Landlord & Empty Property" product *might* — [not confirmed] | Council HIL £1k–£25k subsidised, legal charge, property 10yr+; direct products 5.49–6.49%, secured |
| **FHIL** | **WINDING DOWN — effectively closed** | ~12 (unconfirmed; dead site) | Moot | No new loans since **April 2024**; being dissolved/replaced by a consortium; MK & RBWM already closed [verified: primary — Cherwell DC report 2 Dec 2025] |

**Lendology's 20 empty-property councils** [verified: primary, council selector]: Bath & NE Somerset, Bristol, Cornwall, Dorset, East Devon, Exeter, Merton (LB), Mid Devon, North Devon, North Somerset, Somerset, South Gloucestershire, South Hams, Suffolk (authority TBC), Teignbridge, Torridge, West Devon, West Oxfordshire, West Yorkshire Combined Authority, Wiltshire. It's the growing national consolidator (took on West Oxon from FHIL).

**Parity Trust's 16** [secondary — logos; Wealden & Fareham primary-confirmed]: Basingstoke & Deane, Brighton & Hove, Eastbourne, Eastleigh, Elmbridge, Epsom & Ewell, Fareham, Gosport, Guildford, Hastings, Lewes, New Forest, Runnymede, Rushmoor, Wealden, Woking.

**No single national directory** of council loan schemes exists. **Foundations** (national HIA body; "Find My HIA") points to your local council, not a scheme list; Action on Empty Homes / Empty Homes Network are campaign/practitioner bodies. Lendology's council selector is the single most useful published list. [verified: primary]

**What this lets the lane do:** know that ~36 councils have an OPEN provider-run loan (Lendology 20 + Parity 16) — but all are **owner-improvement**, so they help a buyer only *after* completion (financing works, not the acquisition), and only if the council/provider treats a new owner as an eligible "owner". Confirm purchase-stage eligibility case by case.

---

## §C. The genuinely buyer/investor-friendly money (the real §7 answer)

These carry **no owner-occupation string**, so a buy-renovate-sell (or let) fits:

| Scheme | Area | Type | Terms | Buyer flip OK? |
|---|---|---|---|---|
| **Kent "No Use Empty"** | 12 Kent districts (not Medway) | Interest-free loan | £25k units to £175k/applicant; empty 6mo+; repay ≤3yr (rent) or on sale/24mo | **Yes** — aimed at owners/developers [verified: primary] |
| **Wales "Houses into Homes"** | National (via each Welsh LA) | Interest-free loan | ≤£25k/property, £250k/application, ≤80% LTV, no occupancy string | **Yes** — "anyone can apply" [verified: primary] |
| **Derby City** | Derby | Interest-free loan | £20k; buy as home OR to rent (excludes holiday/serviced lets) | **Yes** [secondary] |
| **Burnley** | Burnley | Interest-free loan | £25k in selective-licensing areas / £20k outside | Yes [secondary] |
| **Warrington / Nuneaton & Bedworth / Stafford / Staffs Moorlands / Boston / Charnwood** | resp. | Low-cost/interest-free loans | £2k–£10k typical | Mostly yes [secondary — verify] |
| **Parity Trust direct "Landlord & Empty Property"** | E.Sussex/Hants/Surrey | Commercial loan | 5.49–6.49%, secured | Possibly — purchase capability [not confirmed] |

**Grants that RULE OUT a flip (occupy/let strings):** Liverpool £5–20k (3-yr council nomination at LHA rent + charge), Rutland £15k (let 5yr at LHA), Wirral £10k (lease back to council 3yr), South Ribble (5-yr let), South Holland £10k (repay if sold within 10yr), and the **Welsh £25k grant** (live there 5yr). Useful only for a hold-and-let strategy, not a resale. [primary for Liverpool/Welsh; secondary for the rest]

---

## §D. Empty-homes grants by region (roundup — flag all as secondary)

Backbone source: propertyinvestmentsuk.co.uk regional lists (amounts may lag — re-check each council page before relying). [secondary]
- **North West:** Cheshire West & Chester (grant £15k / conversion £75k / equity loan), Preston (repair & lease), Ribble Valley £15–20k, Rochdale £15k loan / repair-&-lease, South Ribble £4.5k/room (5yr let), Stockport (≤75%, heritage area), Tameside £28k lease-&-repair, Wirral £10k/£5k, Warrington £10k loan, Burnley loan.
- **East Midlands:** Boston £6k loan, Charnwood £15k grant (let after works), Derby £20k loan, Rutland £15k grant (5yr let), South Holland £10k (10yr clawback), West Lindsey £10k, Harborough (accredited landlords).
- **West Midlands:** Wychavon £15k, Shropshire £10k, Bromsgrove, Dudley (owner-occ or let-to-council), Nuneaton & Bedworth £10k loan, Stafford £10k loan, Staffs Moorlands £2k loan. Birmingham reportedly **no** empty-homes grant.
- **North East / Yorkshire (thin):** Durham ~£15k, York (interest-free loans only), Leeds ("Empty Homes Doctor" advice + potential grant). Coverage gap — flagged.
- **Standalone:** Bath & NE Somerset "No Use Empty" (Lendology loan ≤£30k + £25–£500 small-works grants). Barnsley ~£17.5k (−10% owner contribution) [secondary — PDF unread].

---

## §E. LAHF — a signal of "active" councils (not a buyer grant)

The **Local Authority Housing Fund** funds councils to buy/repair homes for temporary/resettlement housing — **not** accessible to a private buyer, but an allocation marks a council actively acquiring/refurbishing stock. Rounds 1–4 (~£500m / £250m / ~£450–500m / £950m); Round 3 had **203 LAs**. **No single per-council allocation table on gov.uk** — amounts live in individual council cabinet papers (e.g. Croydon £8.1m, North Yorkshire £1.80m, Nottingham £1.72m, Oldham £1.51m, Thanet £0.62m). Source: gov.uk LAHF collection + Round 3 prospectus. [verified: primary for the collection; per-council figures secondary]

---

## §F. Other stacking levers (national, buyer-claimable)

- **5% empty-home VAT** (empty 2yr+) / **zero-rate** sale (10yr+): the biggest lever; council issues the empty-duration (EPO) letter, buyer uses any VAT-registered builder. [verified — Brief 3 item 2]
- **Council-tax premium major-repairs exception:** up to **12 months' relief** from the premium during major/structural repairs, national from **1 Apr 2025** (empty homes); a 12-month probate exception also stacks if inherited. [verified: primary — substance; exact class letters not asserted]
- **SDLT non-residential rate for a genuinely derelict shell:** *Bewley* [2019] UKFTT 65 won (demolition-level dereliction); *Mudan* [2025] EWCA Civ 799 lost ("doer-upper" still residential). High bar — needs structural evidence. [verified: primary — cases]
- **Acquisition channels (deal-flow, not cash):** council/CPO **enforced-sale auctions** (e.g. Rushcliffe, Bolsover) and CPO'd-stock resale with bring-back covenants (Haringey, Burnley, Birmingham); **Empty Homes Matchmaker** lets a private buyer register in a few areas (**Knowsley, Bury** in England — thin inventory; strongest in Scotland). [secondary]
- **Debunked:** there is **no** council-run "approved 5% VAT contractor" panel (Kent NUE only educates owners); housing-association **purchase-and-repair** puts the buyer on the *selling* side (not usable); national capital funds (BLRF3, Homes England) are council/RP-facing. [verified/secondary]

---

## §G. The 20 councils where the most layers stack

Layers scored: **investor-usable finance** (loan with no owner-occupation string = strongest) + **empty premium adopted** (seller pressure) + **second-home premium** + **LAHF-active**. VAT/major-repairs exception apply everywhere, so they don't discriminate. **Resale value is the lane's own data — overlay it before ranking for real; low-value stock (e.g. sub-£200k) can wipe the margin regardless of incentives.** Finance rows marked [secondary] need a per-council re-check.

**Tier 1 — investor-friendly finance + premium (strongest):**
1. **All 12 Kent districts** — Ashford, Canterbury, Dartford, Dover, Folkestone & Hythe, Gravesham, Maidstone, Sevenoaks, Swale, Thanet, Tonbridge & Malling, Tunbridge Wells (Kent NUE interest-free loan, buyer-eligible; premium near-universal). [primary — scheme]
2. **Derby City** — £20k interest-free, buy-to-let allowed. [secondary]
3. **Burnley** — £20–25k interest-free loan + active CPO/enforced-sale programme + low entry prices. [secondary]

**Tier 2 — buyer-usable loan or generous grant + premium (verify finance row):**
4. **Cheshire West & Chester** (grant £15k / conversion £75k). 5. **Warrington** (£10k loan). 6. **Rochdale** (loan/repair-&-lease). 7. **Nuneaton & Bedworth** (£10k loan). 8. **Wychavon** (£15k grant). 9. **Ribble Valley** (£15–20k). 10. **Bath & NE Somerset** (Lendology ≤£30k + small grants). 11. **Charnwood** (£15k grant). 12. **Boston** (£6k loan). [all secondary — verify]

**Tier 3 — Lendology/Parity open (owner-improvement finance) + premium, higher-value stock:**
13. **Bristol**, 14. **Cornwall**, 15. **Wiltshire**, 16. **Dorset**, 17. **North Somerset** (Lendology). 18. **Guildford**, 19. **Woking**, 20. **Wealden** (Parity). [finance = owner-improvement, confirm buyer eligibility at completion]

**Caveats on the shortlist:** it ranks *incentive layers*, not deal quality — the lane must overlay its own resale medians and candidate counts (as in Eric's "where it pays to look" table). Tier-3 finance is owner-improvement only. Kent/NW/E-Mids rows in Tiers 1–2 rest on scheme pages or roundups dated 2026-09-27 and should be re-confirmed on the council's own page before a deal is built on them.

---

## Corrections & unresolved
- **Brief 3 correction:** the buyer-finance framing of Bracknell/Woking/Guildford was overstated — FHIL (Bracknell's route) is winding down; Woking/Guildford are Parity **owner-improvement** loans. No readable regional-lender scheme finances the *purchase* itself.
- **1-year LTE trigger** can't be read nationally from the CTB data for ~34% of councils (fold-in) — per-council page needed for those.
- **Secondary finance rows** (§C–§D regional roundups, Parity partner list, FHIL membership, Barnsley/Newcastle) need per-council re-check; flagged inline.
- **LAHF Round-3 total** (£450m vs £500m) unresolved; no single per-council table published.
