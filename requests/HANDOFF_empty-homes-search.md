# Handoff to Empty Homes Search — cloud research session

**Date:** 27 September 2026 · **From:** cloud research session (external desk research lane).
**Everything below is on `main` in `erictsoi/research`** (repo collapsed to a single branch; no PRs). Rules honoured throughout: external reading only, no FOIs/contact/paid data, no addresses. Claims are tagged [verified: primary]/[secondary]/[inferred] inside each file.

This is an index + the decisions/corrections that matter. Open the named files for detail.

## 1. Deliverables on `main`

| File | What it gives the lane |
|---|---|
| `data/premium_pressure_2025.csv` | **All 296 English councils scored** for empty-homes premium pressure: adoption, inferred trigger (1yr/2yr/unknown), per-tier dwelling counts, statutory premium £ at each tier, second-home premium, 0–100 bite score. From MHCLG Council Taxbase 2025 + Band D. |
| `reports/2026-09-27_premium-pressure-scores.md` | The scoring method, top councils, bite-vs-supply lenses, the 13 boroughs scored, caveats. |
| `reports/2026-09-27_brief4-national-incentives.md` | National incentive stacking: premium data source, regional loan CICs, buyer-friendly finance, other stacking levers, 20-council shortlist. |
| `reports/2026-09-27_gap-resolutions.md` | Latest: 16 priority councils confirmed 1yr-trigger + the six dead-ends resolved (see §4). |
| `reports/2026-09-27_brief3-external.md` | Bona vacantia (BVC2) purchase route, empty-home VAT evidence, council-tax premiums/Band D (13), ONS deaths-by-LA (13), EPC data migration, executor-contact law, empty-homes finance, CPO/EDMO. |
| `reports/2026-09-27_followups-external.md` + `reports/2026-09-27_fca-perimeter-solicitor-brief.md` | Earlier follow-ups (F1/F2/F4/F9/F10/F11/F12) + the FCA-perimeter solicitor brief. |
| `reports/2026-09-26_*` | The three foundation reports (deceased estates & enforcement; address history/logbooks/exits; empty-homes finder programme A–G; insights & follow-ups). |
| `requests/perplexity_council_premium_prompts.md` + `..._targets.csv` | Prompt pack to close the 96 unknown-trigger councils + finance/legal gaps (see §4). |
| `COORDINATION.md` | Running division-of-labour + all decisions to date. |

## 2. Findings that change how the lane operates

- **Gazette coverage ≈ 1 in 5 of the target, not 1 in 14.** The 7%-of-all-deaths figure understates it: against the ~204k owner-occupier homes emptied by a death/yr, 39,100 notices ≈ **~19%**. Misses concentrate in non-targets (renters, surviving spouses, care). The way to widen is more *entry points*, not more death data.
- **"Council money for a buyer" is largely a myth.** Every readable council-partnered loan (Lendology 20 councils, Parity 16, FHIL — winding down) finances an **existing owner improving a home they hold**, not the purchase. This corrects the earlier Bracknell/Woking/Guildford "buyer finance" framing. The genuinely buyer/investor-friendly money: **Kent No Use Empty, Wales Houses into Homes, Derby, Burnley**.
- **Let-to-council grants are a valid exit, not a killed deal.** Liverpool/Rutland/Welsh-grant strings (3–5yr let/nomination) suit buy-refurb-let/refinance; the renovator still profits over a hold.
- **Premium pressure is scored nationally now** (`data/premium_pressure_2025.csv`). Sweet spot (high bite × high supply of premium-charged homes): Liverpool, North Yorkshire, Cornwall, Sheffield, Bradford, Sefton, Cumberland, Birmingham. **Overlay your own resale medians before ranking** — low-value stock wipes the margin regardless.
- **Bona vacantia = a real acquisition path** for the 75 company-limbo homes: the free **BVC2 referral** to GLD (open-market/auction, ~£1k legal + £2.4–4.4k valuer, no title guarantee); a connected party could instead restore the company (£341 admin / £326 court).
- **Gazette disclaimer feed** = `noticetypes=2603` (Companies Act s.1013 Crown disclaimers). Names the property address (not always a title number), commercial-heavy, mixes English + Scottish. Confirmation signal on the company-limbo list, not a primary finder.
- **⚠ EPC data migration is time-critical:** the old `opendatacommunities` service dies ~30 May 2026. Move to `get-energy-performance-data.communities.gov.uk` (GOV.UK One Login bearer token; daily `/api/domestic/search?date_start=`; `TRANSACTION_TYPE` + `TENURE` still present; OGL v3.0) before then.
- **FixMyStreet** 2010–13 test is feasible on the free national Open311 API (no scraping); run it on a high-volume council, not a sparse one; confirm data-reuse licence with mySociety before publishing.

## 3. Owned by the lane / needs your data (not resolvable by desk research)

- **Title checks** — 15 stuck both-gone homes ≈ £105 (£7/register); stuck-vs-inherited can't be read for free. Your batch, your purchase.
- **Per-address facts** — which specific home is stuck vs occupied; council-tax liability changes (not public); per-address premium tier (not public).
- **OS GB Address vs product comparison** — still blocked on a product description from your side.
- **Resale medians / candidate counts / the 2012 empties list** — local by design; overlay onto the premium scores.

## 4. Open items + the way to close them

- **Unknown 1yr-vs-2yr premium trigger — now 80 left (was 96).** The cloud session resolved the **top-17 priority batch (16 confirmed 1yr from council-own pages; Gateshead still `unclear`, likely 2yr)** and the **six non-council dead-ends** via its own web search (Perplexity credits were exhausted). All folded in: see **`reports/2026-09-27_gap-resolutions.md`**, and `data/premium_pressure_2025.csv` is updated (trigger counts now 186 1yr / 80 unknown / 25 2yr / 5 none; Rutland now scores 100). The remaining 80 run the same way from `requests/perplexity_council_premium_prompts.md`.
- **Dead-ends resolved** (in the gap-resolutions report): bona vacantia auctions sell via Allsop under the "Solicitor for HM Treasury" seller name; VAT evidence case *G S Bhachu*; ICO nearest analogue is *Experian* (nothing specific to Gazette-notice reuse); LAHF has no consolidated per-council table; **FixMyStreet report data has no open licence — bespoke/by-arrangement with mySociety (matters before publishing the 2010–13 test)**; Policy in Practice "Missing Out" latest is 2025, no 2026 edition yet.
- **Legal items (VAT buyer-can-get-EPO-letter; executor-outreach lawfulness)** need a solicitor's sign-off — desk research has taken them as far as it can.

## 5. Corrections log (things earlier notes got wrong)
- CPO "~182 register": it's a *derived filter* of the real gov.uk "CPO: register of decisions" (all CPO types, SoS-decided) — not wrong, just clarified.
- Bracknell/Woking/Guildford "buyer finance": overstated — see §2.
- Council-tax premium schedule from the Empty Property Hunters interview ("double yr1, triple ~5yr") was muddled — correct is 100%/200%/300% at 1/5/10yr.
