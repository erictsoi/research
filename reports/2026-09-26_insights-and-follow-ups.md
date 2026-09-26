# Insights and follow-up questions — 26 September 2026

This note sits alongside two reports:
- `reports/2026-09-26_deceased-estates-and-enforcement.md` (council tax for deceased estates; enforcement)
- `reports/2026-09-26_address-history-logbooks-exits.md` (address data history; logbooks; M&A)

**Purpose:** record the conclusions we drew from the reports, and give future sessions self-contained questions to pick up.

**Conventions**
- Tags follow the reports: **[verified: primary]**, **[secondary]**, **[inferred]**.
- Every fact here has its source in the report section cited.
- Anything marked "assumption" is not established.

**Access note.** Sources were reachable in this environment only after the network policy was widened. Still blocked:
- 403: commonslibrary.parliament.uk, hansard.parliament.uk, publications.parliament.uk, questions-statements.parliament.uk, ofcom.org.uk, ifs.org.uk, github.com, costargroup.com, maps.org.uk, moneyhelper.org.uk
- 405: webarchive.nationalarchives.gov.uk
- connection reset: web.archive.org

Workarounds that worked:
- Historic Hansard via `api.parliament.uk/historic-hansard`
- Written questions and statements via `questions-statements-api.parliament.uk`

---

## 1. Key insights

### A. Where the opportunity is

1. **No one recovers council tax specifically for estates.**
   - With full access we found no service that recovers exemption Class F or other council tax refunds for estates.
   - The nearest is Ingram Toft, a general claims firm that includes exemption and discount refunds, at 25% + VAT (capped at £10,000).
   - Source: estates report §5. Confidence: moderate-to-good.
2. **The legal footing is strong, but it isn't automatic in practice.**
   - The Class F exemption needs no claim.
   - Councils must take "reasonable steps" to identify exempt dwellings and must assume exemption when they have "reason to believe" (SI 1992/613 regs 8–9).
   - The first-stage s.16 complaint has no time limit.
   - But Tell Us Once does not apply Class F, and HMRC's own manual says executors are "unlikely, in practice" to get refunds for the whole period since death (IHTM28192).
   - This gap between entitlement and practice is the product opportunity.
   - Source: estates report §§1.7, 2.1–2.3.
3. **Band corrections can reach back to 1993.**
   - Correcting an error in the list as first compiled takes effect "from the day on which the list was compiled", i.e. 1 April 1993 in England (SI 2009/2270 reg 11(7)(b)).
   - The personal representative is entitled to any excess the deceased paid (SI 1992/613 reg 58(4)).
   - So an estate may recover overpayments from the deceased's own years. How far back councils will actually pay is untested.
   - Source: estates report §3.4.
4. **The market is large and mostly unadvised.**
   - 570,988 deaths in England and Wales in 2025.
   - 239,091 probate grants in 2025.
   - About 44% of probate grants go to personal (non-professional) applicants.
   - About 12% of probate applications are made more than a year after death.
   - Our estimate of homes left empty by a death is about 190–210k a year. **[inferred; two assumptions unverified]**
   - Source: estates report §4.
5. **Errors can't be fixed once enforcement starts.**
   - A wrong band or a missed discount "may not be raised" at the liability order hearing (SI 1992/613 reg 57(1)).
   - About 1.72m council tax cases went to bailiffs in 2025/26.
   - Bailiff fees rose on 1 May 2026 (£79 compliance, £247 enforcement).
   - So the value is in catching errors before the summons.
   - Source: estates report §§6–7.
6. **Unclaimed help is large.**
   - About £3.3bn of Council Tax Support goes unclaimed across Great Britain (Policy in Practice 2025).
   - Pensioners in England miss about £1.7bn of Council Tax Reduction, at 50% take-up (Independent Age, June 2026).
   - Source: estates report §8.
7. **Council-tax-only checking appears to sit outside FCA regulation.**
   - The regulated debt activities (arts 39D–39E of the Regulated Activities Order) are tied to credit agreements.
   - Council tax refunds aren't a regulated claims-management category (art 89G).
   - The line is crossed when advice covers credit debts too (PERG 17.3 Q3.3).
   - Needs a regulatory lawyer's sign-off.
   - Source: estates report §9.

### B. Why property data is still poor (useful for pitch framing)

8. **The council tax list rests on a rushed 1991–93 exercise.**
   - About 21m homes were banded mostly "at the desk"; the VOA's own manual says "Very few properties were externally inspected".
   - In April 1993 the VOA didn't know the property type for 35% of homes or the build period for 37%.
   - Its own challenge form asks owners to "estimate" the year the property was built.
   - About 1.31m bands have been cut on challenge since 1993.
   - Source: address report §§1, 4.3.
9. **UPRNs are free but addresses aren't.**
   - Since July 2020, OS Open UPRN has been free under the Open Government Licence, but it has no address text.
   - Address text needs AddressBase or OS GB Address, and Royal Mail postcode-file (PAF) licence terms.
   - Government pays £30.8m (2023–28) to Royal Mail so public bodies can use the PAF free.
   - Source: address report §§2.5–2.6, 3.
10. **Key datasets still aren't joined up.**
    - Land Registry price-paid data gained a UPRN lookup only on 28 August 2026, and only for new records.
    - The VOA refused under FOI (2025) to publish its lookup between its own record numbers (UARNs) and UPRNs.
    - Source: address report §§4.1, 5.

### C. The AddressBase replacement (OS GB Address), and what it means for us

11. **What's changing.**
    - AddressBase and AddressBase Plus reach end of life in autumn 2027. OS GB Address replaces them.
    - It is built from OS's National Geographic Database and contains everything in AddressBase Premium.
    - Source: address report §2.4a. **[verified: primary]**
12. **What OS GB Address adds:**
    - daily updates;
    - separate records for planned, live and demolished addresses, with dates and snapshots of past dates;
    - floor levels, and links from each flat to its building's UPRN;
    - Royal Mail matching, with a reason recorded when an address doesn't match;
    - cross-references from each UPRN to OS buildings and land, and to the **VOA council tax record number (UARN)**.
    - **[verified: primary]**
13. **What it doesn't do:**
    - no council tax band;
    - no property details (rooms, build year, extensions, condition);
    - no link to Land Registry titles;
    - still a paid licence, with PAF terms on the address text.
    - **[verified: primary for the fields read; absence of a band field checked in the Built Address schema]**
14. **What it means for us.** **[inferred; assumption about our product]**
    - OS GB Address is infrastructure to build on, not a competitor.
    - The VOA record-number cross-reference is new and useful: it gives licensed users the UPRN ↔ council tax record link that the VOA refused to publish under FOI.
    - Our value would sit on top of it:
      - whether the band is right;
      - what the property is actually like;
      - who is liable, and which exemptions apply (e.g. Class F);
      - recovering the money.
15. **Policy has dropped UPRN.**
    - MHCLG's October 2025 consultation proposed a core logbook data set "linked to the Unique Property Reference Number (UPRN)". The June 2026 roadmap doesn't mention UPRN or BASPI.
    - The Open Property Data Association's framework API is keyed on UPRN. The Residential Logbook Association being keyed on UPRN is claimed only by a third party.
    - This is an open standards question worth influencing.
    - Source: address report §§6, 8.

### D. Exit and comparables

16. **Deals with published figures.**

    | Target | Buyer | Year | Price | Multiple |
    |---|---|---|---|---|
    | Groundsure | InfoTrack's parent | 2021 | £170m | ≈8.5x revenue |
    | TM Group | Dye & Durham, then resold to AURELIUS | 2021 / 2023 | £91.5m; resold for £50m + up to £41m earn-out | — |
    | OnTheMarket | CoStar | 2023 | £99m | ≈2.9x revenue |
    | Smoove | PEXA | 2023 | £30.8m | ≈1.5x revenue |
    | Rightmove | REA Group (approach lapsed) | 2024 | £6.2bn | 22.7x EBITDA |
    | Hometrack | Providence (pending) | 2026 | undisclosed; reported ≈£600m | ≈10x revenue (Asymmetrix estimate) |

    - Source: address report §11.
17. **Several comparables in the brief aren't real deals.**
    - Landmark was not sold to Astorg; it is still owned by DMGT.
    - "PropertyData" and "Land Insight" deals found online are Australian firms.
    - No sale was found for TwentyCi, Sprift, Nimbus Maps, Searchland or Moverly.
    - Source: address report §11.
18. **Sector multiples.**
    - The only dated published source (Fortlane, September 2025) gives medians of 8.5x revenue and 22.7x EBITDA.
    - Listed peers have de-rated: Rightmove trades at about 10.9x EBITDA today (third-party data).
    - Source: address report §12.

---

## 2. Follow-up questions for other sessions

Each item stands alone.

- **Start with:** the report section named in "Context".
- **Tag every claim** as the reports do.
- **Record results** in a new dated report under `reports/`, or append to the relevant report, and tick the item here.

### Priority 1 — would change a decision

- [ ] **F1. Refund time limit (legal).**
  - **Question:** Can a council cap repayment of Class F or band-correction overpayments at 6 years? Cover SI 1992/613 reg 31, Limitation Act 1980 ss.5, 9 and 32(1)(c), and *AXA Insurance v HMRC* [2026] UKSC 24.
  - **Context:** estates report §2.3.
  - **Done when:** we have case law, VTE decisions or ombudsman decisions on how far back councils actually repay, plus a solicitor-ready summary.
- [ ] **F2. What do councils actually do?**
  - **Task:** Sample 20–30 English councils' Class F and refund pages and policies.
  - **Questions:**
    - Do they backdate?
    - Do they apply a 6-year cut-off?
    - Do they act on Tell Us Once alone?
    - What evidence do they ask for?
  - **Context:** estates report §§1.7, 2.
  - **Done when:** a table of councils × practices, with URLs.
- [ ] **F3. Recovering the deceased's own years after a band correction.**
  - **Question:** After a correction backdated to 1993 (reg 11(7)(b)), do councils refund earlier taxpayers or their estates (reg 58(4)), and how far back?
  - **Where to look:** council policies, VTE decisions, MSE forum reports.
  - **Context:** estates report §3.4.
- [ ] **F4. FCA perimeter sign-off.**
  - **Task:** Draft the questions for a regulatory lawyer on council-tax-only checking and negotiation (RAO arts 39D–39G; PERG 17.3 Q3.3), including where a customer script must stop and refer on.
  - **Context:** estates report §9.
- [ ] **F5. Our product vs OS GB Address.**
  - **Needs:** a description of our product from the user.
  - **Task:** A feature-by-feature comparison, and a decision on whether to license OS GB Address, AddressBase Premium or AddressBase Core, and the cost of each.
  - **Context:** address report §2.4a; §1C above.
- [ ] **F6. OS GB Address pricing and licensing.**
  - **Questions:**
    - What does a commercial licence cost (OS Data Hub premium, or OS partners)?
    - Is OS GB Address included in the PSGA for public bodies?
    - Does using the VOA record-number cross-reference carry any VOA or HMRC terms?
  - **Context:** address report §2.4a.

### Priority 2 — strengthens evidence

- [ ] **F7. The 1994 NAO report** *Council Tax Valuations in England and Wales* (HC 1993-94 320).
  - **Task:** Get staff and contractor numbers, inspection rates and the accuracy audit.
  - **Access:** blocked at webarchive.nationalarchives.gov.uk (405). Try the British Library, a parliamentary papers library, or ask the NAO directly.
  - **Context:** address report §1.4.
- [ ] **F8. Does the VOA band-check result page show a UPRN or a council reference?**
  - **Access:** blocked for scripted access (403). Needs a manual check in a browser.
  - **Context:** address report §4.2.
- [ ] **F9. Liability order counts.**
  - **Task:** Find an official source (HMCTS management information, PQs via questions-statements-api, FOI) to replace the dropped "2.4m" figure.
  - **Context:** estates report §6.
- [ ] **F10. Time from grant to sale, and probate sales per year.**
  - **Where to look:** HMLR price-paid data joined to probate data, or industry data (Rightmove, TwentyCi).
  - **Context:** estates report §4.
- [ ] **F11. Test the empty-homes estimate (~190–210k a year).**
  - **Task:** Use ONS deaths by marital status and living arrangements, and care-home residents' tenure.
  - **Context:** estates report §4.
- [ ] **F12. Updated unclaimed-benefit figures.**
  - **Task:** Check whether *Missing Out 2026* (Policy in Practice, due September 2026) replaces the £3.3bn Council Tax Support figure.
  - **Context:** estates report §8.
- [ ] **F13. Commons Library and IFS material.**
  - **Task:** Get CBP-10651 (empty homes after a death), the council tax revaluation briefings, and IFS's 2020 revaluation report.
  - **Access:** blocked (403) here. Try from another environment.
  - **Context:** both reports.

### Priority 3 — watch list (things due to change)

- [ ] **F14. MHCLG delivery.**
  - **Task:** Check for the non-statutory listings guidance, the Code of Practice for agents, and the standard material-information form promised for 2026.
  - **Context:** address report §§6, 10.
- [ ] **F15. Smart data.**
  - **Task:** Look for the outcome of DBT's multi-sector call for evidence (closes 1 October 2026), and whether MHCLG issues its own property call for evidence.
  - **Context:** address report §9.
- [ ] **F16. HM Land Registry logbook trial.**
  - **Task:** Name the four logbook providers taking part, and track the results (the trial runs June 2026 to about June 2027).
  - **Context:** address report §7.
- [ ] **F17. England council tax reforms.**
  - **Task:** Track the statutory instrument for the 63-day rule, the £100 costs cap and 12 instalments (due from April 2027), and the outcome of the July 2026 technical consultation.
  - **Context:** estates report §7.
- [ ] **F18. Wales.**
  - **Task:** Check for any further amendments to the Class F exemption after WSI 2026/118 (in force 30 October 2026).
  - **Context:** estates report §1.6.
- [ ] **F19. Hometrack deal.**
  - **Task:** Confirm completion and any disclosed price or revenue. Also watch for a Zoopla or Alto sale.
  - **Context:** address report §11.
- [ ] **F20. OS Royal Mail Address v2.0 (due early October 2026).**
  - **Task:** Confirm what the "Not Yet Built" and "Multiple Residence" content adds.
  - **Context:** address report §2.4a.

### Needs the user

- [ ] **U1.** Describe our product and target customer (estates, households facing enforcement, logbooks, data licensing) so that F5 and positioning can be done properly.
- [ ] **U2.** Decide which branch should be the repository's main branch, so pull requests can be opened.
