# Empty-homes finder: free public signals, market, economics and levers

**Date:** 26 September 2026
**Scope:** England. Wales is noted where it differs.
**Commissioned by:** the "YouTube transcript mining" session, on Eric's behalf.
**Finder constraint:** free public sources only. No paid data, no FOI, no asking people. The research itself read any public source.

## How to read this report

**Tags**
- **[verified]**: checked at source this session. Key wording is quoted in the working notes.
- **[claimed]**: comes from a secondary source, a search extract, or a vendor's own claim.

**Verdict:** each finding is rated **usable by a free-only finder: yes / partly / no**.

**Working notes (session scratchpad):** `notes/eh_A.md`, `eh_A0.md`, `eh_A000.md`, `eh_B.md`, `eh_C.md`, `eh_D.md`, `eh_EF.md` and `eh_G.md`. They hold fuller quotes and URLs.

**⚠ Probate search.** The free search at probatesearch.service.gov.uk shows only name, date of death, date of probate, probate number, document type and registry. It shows **no address** [verified]. A separate data-access concern about that service has been passed to Eric for responsible disclosure. **The finder must use nothing beyond what the public page shows.**

---

## The three most actionable findings

**1. The Gazette's deceased-estates feed is the best free source of lead addresses. Usable: yes.**
- **What it gives:** Trustee Act 1925 s.27 notices carry the deceased's **address, full postcode, a map point and the date of death**.
- **Access:** a free Atom/data feed with no key, e.g. `https://www.thegazette.co.uk/all-notices/notice/data.feed?noticetypes=2903&start-publish-date=…&end-publish-date=…`.
- **Volume:** about **39,058 notices in 2025**, roughly 7% of deaths.
- **Terms:**
  - Licence is OGL, but it **excludes personal data**, so data-protection duties apply.
  - Fair use is **5 requests per 10 seconds**, with crawling only **9pm–7am**.
- **Care homes:** about 6–13% of sampled notices give a care-home address; filter these out.
- **Limitation:** notices exist only once someone is administering the estate.
- **Pipeline:** Gazette notice → match the name in the free probate search, as displayed → join to Price Paid (last sale) and EPC (lodgement age) by UPRN → rank.
- [verified] `notes/eh_A.md`

**2. Council tax base counts show where stuck estates cluster. Usable: yes, for area weighting.**
- **Class F (owner has died), England:** **124,064** dwellings at 6 Oct 2025 (MHCLG *Council Taxbase 2025*).
  - Trend: rose from 76.6k (2015) to a **135.7k peak in 2023**, then fell as the probate backlog cleared.
  - Top councils by count: Birmingham 2,106, Cornwall 1,808, North Yorkshire 1,707.
  - Top councils per 1,000 dwellings: Adur, Rother, Worthing (about 9, against an England average of 4.8).
  - Source: https://www.gov.uk/government/statistics/council-taxbase-2025-in-england [verified]
- **Long-term empty:** **303,185** in October 2025, up 14.5% in a year. **152,928** pay the premium. [verified]
- Use these to target councils and wards before looking at individual addresses.

**3. Free datasets that give addresses directly. Usable: partly.**
- **Council public-health funeral datasets** (funerals the council arranges when no one else does). About 26 councils publish them on data.gov.uk.
  - Calderdale gives **full street address and postcode**, estate value and whether the case went to the Treasury Solicitor: https://dataworks.calderdale.gov.uk/dataset/public-health-funerals-2yk67 [verified]
  - Barnet gives a postcode district. Dudley, Peterborough and Hull withhold addresses because of burglary risk. [verified]
  - Treat results carefully: delay or suppress them.
- **MHCLG compulsory purchase register:** **178–182 empty individual houses since 2019**, each titled by address. https://www.gov.uk/government/publications/compulsory-purchase-orders-register-of-decisions [verified]
- **Gazette disclaimer notices** (property given up by a liquidator or the Crown): **913 in 2025**, with title number and address. [verified]
- **Company-owned homes of dissolved companies:** CCOD minus the live Companies House register gives candidates. Licence caveat: CCOD allows internal scoring only; it restricts address reuse and forbids contacting owners. [verified]

---

## G. Seeing estates where probate was never started

**Finding:** there is **no free public list** of deaths where probate was never started. [verified]

| # | Lead | Verdict at source | Free? | Bulk? | Address? | Usable |
|---|---|---|---|---|---|---|
| G1 | **Public Trustee notices register.** LP(MP)A 1994: s.14 substituted AEA 1925 s.9 (vesting in the Public Trustee); s.18 makes service on the Public Trustee count. ⚠ s.17 is "absence of knowledge of intended recipient's death", not "no personal representative". Search is by the deceased's **name only**, form NL2 (in practice by email): **£20 per search**, **£40 to register a notice**. No statistics published since the 2013-14 annual report. | [verified] with brief corrected | No (£20) | No | Only if you already know the name | **No** |
| G2 | **Death-notice sites.** funeral-notices.co.uk: 0 house numbers in 22 sampled notices, typically town level. Terms: "for personal and non-commercial use only" (https://funeral-notices.co.uk/terms_conditions). legacy.com/uk returned 403. iannounce.co.uk no longer resolves. | [verified] | Yes to read | No (terms) | Town only | **Partly**: name + date + town, then check for a grant |
| G3 | **Unclaimed estates list** (Government Legal Department). Free CSV, updated most working days, 5,504 rows. Five columns only: ref, forename, surname, date of death, place of death (town + postcode district). Fields were cut after a July 2025 suspension over fraud. Covers intestate, no-kin estates of £500+ only. https://www.gov.uk/government/statistical-data-sets/unclaimed-estates-list | [verified] | Yes | Yes (CSV) | District only | **Partly** |
| G4 | **How creditors learn of a death and collect** (see breakdown below) | [verified] | — | — | — | Mostly **no** |
| G5 | **Class F with no grant ever made.** England has **no time limit** before the grant (SI 1992/558 art 3). Wales has a **2-year cap** before the grant from 1 April 2026 (WSI 2026/8). Counts per council are published (see finding 2). **No council or national source publishes counts by how long a property has been exempt.** | [verified] | Yes | Yes | No | **Partly** (area weighting) |

**G4 breakdown: is any trace public?**
- **Private channels, no public trace:**
  - Death Notification Service (banks)
  - Tell Us Once (government)
  - Bereavement Register
  - Mortascreen and similar suppression files
- **Court routes, not public:**
  - A creditor applying for a grant, or issuing a citation or caveat.
  - Probate standing searches: £4, private to the applicant.
- **Rule update:** the rule for appointing someone to represent an estate with no personal representative is now **CPR 19.12**, not 19.8.
- **County court lists:** daily lists on the Courts and Tribunals hearings service are free. They show party names and "Possession", but **no address**. Automated collection needs an HMCTS data licence, and robots.txt blocks it. https://www.court-tribunal-hearings.service.gov.uk/ Usable: **partly**, by hand only.

**What this means in practice:**
- Never-started estates can only be found **indirectly**. Start with a free name-and-town lead (death notice, unclaimed estates list), check it against probate search (no grant), then look for a property signal (no sale in Price Paid, no new EPC).
- Council public-health funeral data is the only free source found that gives a **street address**. [inferred from above]

---

## A. Free per-dwelling signals of vacancy

**Summary:** no free national product flags a dwelling as empty, and no council publishes its per-address empty-homes list. Camden refused in September 2025, and Wigan in 2025, both on crime-prevention grounds. [verified]

### A0. Council notice registers online (s.215 untidy land, dangerous structures, EDMOs, empty-home CPOs)

**Enforcement registers**
- The statutory planning enforcement register (DMPO 2015 art 43) does **not** have to include s.215 notices; where they appear, it's voluntary. [verified]
- **Idox enforcement search:** 18 councils offer an s.215 option. Examples: Leeds, Blackpool, Ealing, Tower Hamlets, Brent, Lambeth.
  - Blackpool returned 33 cases since 2023, many titled "Poor condition of empty property". [verified]
  - Idox's robots.txt is `Disallow: /`, so check by hand; don't harvest with a bot.
- **Published lists:**
  - **Harborough:** PDF register with s.215, served date and address. https://www.harborough.gov.uk/downloads/download/1443/planning_enforcement_register_of_issued_notices [verified]
  - **Merton:** HTML list. [verified]
  - **Harrow:** PDF, stale (2019). [verified]
  - **Cornwall:** a dangerous-structures PDF; the only one found. [verified]
  - Roughly 10 more councils are **[claimed]** (e.g. Scarborough / North Yorkshire, Hinckley & Bosworth). Per-council URLs are in `notes/eh_A0.md`.
- **EDMOs:**
  - Only **11** tribunal decisions on GOV.UK, the latest from 2022.
  - EDMOs must go on each council's licensing register, but councils only have to make it viewable at the office. [verified]
- **National aggregator: none.**
  - planning.data.gov.uk has 222 datasets but none for enforcement, s.215, dangerous structures, EDMOs or CPOs.
  - PlanIt covers planning applications only.
  - Local land charges search is free per address with an account; an official certificate costs £15.
  - Public Notice Portal (publicnoticeportal.uk) aggregates local-newspaper statutory notices, including CPOs and a "Probate & Trustee" category. Its terms are unread.
  - [verified]
- **Verdict: partly.** Manual checks per council, plus the national CPO register.

### A00. Probate search: what is free

- **Free results show:** last name, first name, date of death, **date of probate (the grant date)**, probate number, document type (PROBATE / ADMINISTRATION / Admon with Will) and registry office. **No address.** [verified]
- **Copy cost:** **£16**, not £1.50. Postal search £16; standing search £4. https://www.gov.uk/search-will-probate [verified]
  - The £1.50 figure is the edited electoral register fee per 1,000 entries.
- **Bulk access:** no bulk offer, published API or data-sharing scheme exists. The 1858–1995 calendar is on Ancestry, which is paid. [verified / claimed]
- **Verdict: partly.** Manual lookups confirm that a grant exists and when it was made, and give no address. See the ⚠ note at the top.

### A000. FixMyStreet (mySociety)

**Open311 API** (free, no key): `https://www.fixmystreet.com/open311/v2/requests.json?jurisdiction_id=fixmystreet&agency_responsible=<MapIt id>&start_date=…&end_date=…`. North Lincolnshire's MapIt id is 2591; searching by council name returns nothing. [verified]
- **Fields:** id, lat/long, category, title, description, dates, status, receiving council, photo URL, and reporter name if public.
- **Paging:** a maximum of 1,000 results per query (the newest), so query in monthly windows.
- **Other endpoints:**
  - RSS: last 20 items only.
  - `/report/ajax/<id>`: adds the typed postcode.
  - Map `/around`: returned 503.
  - Dashboard CSV: staff only.

**Terms**
- robots.txt: crawl-delay 3, disallows `/photo/` and `/report/new`.
- **No open licence** found for report content.
- Free text often contains names and addresses, so treat it as personal data.
- mySociety publishes LSOA-level counts; point-level research data needs an application.

**Categories vary by council.** North Lincolnshire and Leeds have 21 basic categories. FixMyStreet Pro councils (Bromley, Buckinghamshire, Oxfordshire, Peterborough) add private-land vegetation, waste and abandoned-vehicle categories. "Empty Homes" categories exist but have no public reports. [verified]

**North Lincolnshire**
- Reports go back to April 2007.
- Yearly counts: 47 (2010), 37 (2011), **53 (2012)**, 85 (2013), 102 (2014).
- The 2012 reports are mostly street lighting and potholes: 2 fly-tipping, 2 abandoned vehicles, 3 trees.
- There is no North Lincolnshire FixMyStreet Pro site, and the council's own site blocks automated access. [verified]

**Validation**
- Spatially join reports within 25 m and 50 m of the 753 empties, compared against matched controls.
- Expect fewer than 5 hits, so this test is underpowered. Test instead on a busy FixMyStreet Pro council with recent data.

**Other portals:**
- FixMyStreet Pro councils' reports appear on fixmystreet.com.
- Love Clean Streets shows reports publicly only if the council chooses.
- Council "report an empty home" forms publish nothing.

**Verdict: partly** (weak signal).

### Vehicle checks (a car left on the drive)

**DVSA MOT history API** [verified]
- Access: free key; individuals can register.
- Limits: 500,000 calls a day, burst 10, 15 requests per second.
- Endpoints: by registration, by VIN, and a **weekly bulk download plus daily updates**.
- Returns: make, model, colour, fuel, date first used, test dates and results, odometer readings and defects. **No keeper and no address.**

**DVLA Vehicle Enquiry Service API** [verified]
- Returns: tax status (including **SORN**), tax due date, MOT status, make, colour, year of manufacture, and date of last V5C.
- **New registrations are currently closed.** The public "check if a vehicle is taxed" page still works one plate at a time.
- Keeper data (KADOE) is not available to a finder. [claimed]

**Law and practicality**
- The ICO treats a number plate as potentially personal data. [verified]
- Google's terms bar extracting plates from Street View. [claimed]

**Verdict: partly (weak–moderate).** A SORN car with a stale MOT can back up an address found another way, but it needs someone to actually see the car.

### Other signals

| Signal | Grain | Cost / access | Flags an empty by… | Usable |
|---|---|---|---|---|
| **Gazette s.27 deceased estates** | Address + postcode + point | Free feed; fair use applies | Estate being administered | **Yes** (top pick) |
| **Gazette disclaimers** | Address + title number | Free feed | Company or Crown has given up the property | **Yes** (small volume) |
| **CCOD/OCOD** + Companies House live file | Title / address | Free with account; restrictive licence | Company owner dissolved → property passes to the Crown | **Partly** (internal scoring) |
| **Price Paid Data**; PPD→UPRN lookup (first published 28 Aug 2026, new records only) | Address / UPRN | Free, OGL, with address-reuse limits | Long time since last sale | **Partly** (ranking) |
| **EPC register** | UPRN | Free; UPRN is OGL, address fields restricted | Old EPC or no EPC | **Partly** (ranking) |
| **DESNZ postcode energy consumption** | Postcode | Free | Meter counts and low use per postcode | **Partly** (weak) |
| **Business rates lists with empty flag** (Camden, Leeds, Wakefield, Barnet, Blackpool, Croydon, Portsmouth) | Address | Free; licences vary (Blackpool personal use only; Leeds CSV columns shifted) | Empty shop, possibly with an empty flat above | **Partly** |
| **Local land charges** (EDMOs, s.215) | Address | Free per-address search with an account; £15 official certificate | Registered notice | **Partly** (manual) |
| **OS "Unoccupied / Vacant / Derelict" flag** | UPRN | **Paid** product | Explicit status | **No** |
| **Open electoral register** | Address | **Paid** (sold by councils) | — | **No** |
| **London Fire Brigade incidents** | Address blanked for dwellings | Free | — | **No** |

---

## B. The UK empty-homes market (beyond Land Attic, Empty Property Hunters, Grafton, Finders International and Resonance)

**Headline finding:** **no one found publicly claims to detect residential empties from data and sell them to investors, apart from Land Attic.** That looks like an open gap. [verified from operators' own pages; absence is inferred]

| Operator | What it does | Lead source | Data-driven? | Pricing / scale | Tag |
|---|---|---|---|---|---|
| **You Spot Property** (08620615, inc. 23 Jul 2013) | Crowdsourced spotters; cash buyer | Human spotters | No | "£20 gift voucher" per spot + "1% of purchase price (up to £10,000)"; "paid our spotters over £1,000,000" | [verified] https://youspotproperty.com/ |
| Probate.Auction Ltd (15484922); Greenlight Empty Homes Ltd (10043755) | Same group as You Spot Property (shared directors: Kalms, Radstone) | Probate auctions; empties | No | — | [verified] Companies House |
| **Empty Property Experts** | Spotter scheme | Human spotters | No | £20 + up to £10k | [verified] |
| **Property Saviour** (Collingtree Ltd, 07281403) | Cash buyer + spotters | Human spotters | No | £2,000 flat fee on completion; buys at 70–80% of value | [verified] |
| **Property Filter** (13311178) | Investor search tool | Data (probate, "void") | **Yes (investor-facing)** | £100–£250 a month; claims 1,800+ users | [claimed] https://property-filter.co.uk/footer/goal-find-off-market-properties |
| **PropMarker** (13152515) | Probate leads with names of the deceased and administrator | Probate data | Yes | Site says "launching soon" | [claimed] |
| **GalimAI / DealBrief** | Company-owned property only | CCOD / Companies House | Yes (companies only) | £49 / £199 a month | [claimed] |
| **AuctionRadar** | Probate auction lots | Auction listings | Yes (listings) | From £19 a month | [claimed] |
| **Nimbus Maps** | Vacancy flags for commercial property only | Data | Yes (commercial) | Subscription | [claimed] |
| **Datatank / Infoshare+** (04111483) | Verifies empties that councils have listed | Council data + credit bureau | Yes (**councils only**) | "£1.95 to £3.25 a unit"; doesn't sell lists to investors | [verified] https://www.datatank.co.uk/empty-homes/ |
| **OccupID** (Marks Out Of Tenancy, 09535920) | Occupancy estimates for councils | "Over 70" FCA-regulated sources | Yes (**councils only**) | — | [claimed] |
| **HouseBought4Cash**, **Property Solvers** | Cash buyers | Ads, SEO | No | ~80% / 70–80% of market value | [verified / claimed] |
| **Fraser & Fraser, Anglia Research** | Heir hunters; also trace owners for councils | Bona Vacantia, research | No | Often free to councils; commission from the inheritance | [verified] |
| **Latch** (112 homes), **Canopy** (~80), **Giroscope** (Hull) | Charities that buy and renovate | Council partnerships | No | — | [verified / claimed] |
| New, not researched: Empty Property Seller Ltd (Nov 2025), Cornerstone Empty Homes Ltd (Oct 2025) | — | — | — | — | [verified: Companies House listing only] |

**Other notes**
- Raw lead sources in the market are probate grants, the free Bona Vacantia list, Land Registry, Companies House and bulk mail.
- FOI requests for council empty lists are usually refused.
- None of the companies checked show turnover in public accounts; all file small-company accounts.
- Full table: `notes/eh_B.md`.

---

## C. Stuck-estate economics

- **Estates never administered:** there is **no published count**. [verified absence]
- **Official probate timing (HMCTS REDS, March 2026)** [verified]:
  - About 70% of applications are made within 6 months of death, and **12% after more than a year**. The bands stop at ">1 year".
  - **34%** of applications are "stopped" at least once.
  - 1,000–3,500 a quarter go dormant after 6 months with no action from the applicant.
- **Backlog (FCSQ):** the open probate caseload is **rising again**, reaching **47,003 at Q2 2026**. Of these, **3,061 had been open 12–24 months** and **1,566 for more than 24 months**. [verified]
- **Longer delays:** MoneyWeek's "88 → 203 applications taking nearly two years" traces to a Quilter FOI (application to grant, not death to grant). It is **[claimed]**. The PQ 24953 table exists but was blocked.
- **Disputes** [verified unless marked]:
  - Contentious probate claims: **127 in 2025**.
  - Inheritance Act 1975 claims in the Chancery Division, London: **230 in 2025**, up from 158 in 2016.
  - Caveats: 11,328 in 2025 [claimed; Irwin Mitchell FOI].
  - **TOLATA s.14 orders (forced sale between co-owners) and applications to remove a personal representative are not counted separately in any published statistics** [verified].
- **Unclaimed estates:** 5,504 in the list, only about 150–200 per year of death. [verified]
- **Death to sale:** no official data. Trade sources say 9–18 months. [claimed]
- **Class F residence time:** a rough estimate of 6–10 months, calculated as stock divided by an assumed inflow. [inferred]
- Full notes: `notes/eh_C.md`.

---

## D. Council-side levers

**1. Open empties data** [verified]
- Area-level only: MHCLG Council Taxbase / Live Table 615.
- **Long-term empty, England: 303,185** (October 2025).
  - Trend: 203,596 in 2015; +14.5% in the last year. Part of that rise may be councils reviewing records as the new premiums arrive.
- **Top 10 councils:**

  | Council | Long-term empty |
  |---|---|
  | Birmingham | 7,060 |
  | North Yorkshire | 4,652 |
  | Liverpool | 4,492 |
  | Durham | 4,182 |
  | Leeds | 3,932 |
  | Cornwall | 3,667 |
  | Bradford | 3,414 |
  | Barnet | 3,277 |
  | Kirklees | 3,265 |
  | Westmorland & Furness | 2,715 |

- London: 47,287.
- Leeds, Calderdale and Plymouth publish ward or city totals.
- **No council publishes per-address domestic empties.**

**2. EDMO and CPO counts** [verified]
- Neither MHCLG nor MoJ publishes EDMO counts.
- A parliamentary answer (May 2025) gave tribunal receipts of **10, 5, 3, 0, 0** for 2019/20 to 2023/24.
- **11** EDMO decisions are published, 2019–22: Central Bedfordshire, Portsmouth, Northumberland and others.
- **CPO register: 182 house CPOs since 2019.** Burnley (48) and Bradford (32) lead.
- No national data on enforced sales was found.

**3. Council schemes (buyer and partner market)**
- **Kent No Use Empty:**
  - Interest-free loans up to **£175k**.
  - **9,215 homes** brought back into use.
  - https://www.no-use-empty.org.uk/
  - [verified]
- **Bristol:** loans up to £60k at 4%, with 5 years of letting required. [verified / claimed]
- **Cornwall:** loans up to £25k. [verified / claimed]
- **Liverpool:** grants of £5k–£20k in return for tenant nominations at Local Housing Allowance rent. [verified / claimed]
- **Greater Manchester:** an **£11.7m** fund to lease or repair up to 400 homes. [verified / claimed]
- **Bury:** runs a buyer "matchmaker" scheme that takes buyer registrations. This is a direct channel for Eric. [verified / claimed]
- **Wales:** £50m national grants of up to £25k, **for owner-occupiers only**. [verified / claimed]

**4. Premium take-up (Council Taxbase, October 2025)** [verified]
- **291 of 296** councils charge a premium.
- 285 charge 100%, 272 charge 200%, 267 charge 300%.
- The 2026-27 council tax levels release has no premium counts.

Full notes: `notes/eh_D.md`.

---

## E. VAT reliefs on empties

**Legal references (corrected)** [verified]
- **5% reduced rate** after 2+ years empty: **VATA 1994 Sch 7A Group 7, Note 3**. Group 6 is conversions. The period was cut from 3 years to 2 from 1 Jan 2008 by SI 2007/3448.
  - HMRC Notice 708, **section 8**; evidence at **8.3.2**.
- **Zero rate** on the first sale of a dwelling empty 10+ years: **Sch 8 Group 5 Item 1(b), Note 7**.
  - Notice 708, **section 5** (5.3.2–5.3.4).
  - The Notice is internally inconsistent: 5.3.3 measures the 10 years up to the start of works, while Note 7 measures them up to the sale.
  - https://www.gov.uk/guidance/buildings-and-construction-vat-notice-708

**Evidence HMRC accepts** [verified]
- Any of: electoral roll, council tax records, utility records, or a **letter from the council's Empty Property Officer** (enough on its own).
- Squatters, property guardians and storage use don't count as occupation. Second-home use disqualifies.
- The 2 years must run up to the start of works (VCONST07420), and each contractor is tested separately. https://www.gov.uk/hmrc-internal-manuals/vat-construction/vconst07420

**Can public data supply the evidence? No.**
- There is no free per-address proof that a home was unoccupied.
- Councils refuse lists of empty addresses under FOIA s.31, upheld in *Val Blake v IC* [2022] UKFTT 514 (GRC).
- The finder can only shortlist; the Empty Property Officer's letter is the route to evidence. [verified]

**Other taxes** [verified]
- **SDLT:** no relief for empty or uninhabitable homes (SDLTM00385; *Mudan* [2025] EWCA Civ 799).
- No empty-homes relief under Welsh LTT or Scottish LBTT.
- **Council tax:** Class A exemption was abolished in 2013. From April 2025, premium exception **Class M** (major repairs) gives a buyer doing major works 12 months without the premium, and the 12 months restart with each sale.

---

## F. Long-term-empty premium and over-banding (brief, as requested)

**Scale of the premium (Council Taxbase 2025)**
- **152,928** long-term empties pay the premium in England: 58,631 at 1–2 years, 68,673 at 2–5, 17,179 at 5–10 and 8,445 at 10+.
- **7,622 pay 300%.**
- Birmingham has the most (5,193).

**Challenging the band**
- A buyer can make a formal proposal within **6 months** of becoming the taxpayer (SI 2009/2270 reg 4(4)–(5)).
- The premium multiplies any over-banding.
- Deletion from the list needs the house to be "truly derelict" (*Wilson v Coll*), or works actually under way (*Newbigin v Monk*, applied to council tax in *Bunyan v Patel* [2022] and *Harnoczi* [2026] EWHC 993).
- Deletion appeals mostly fail: 67 of the latest 80 were dismissed.

**Valuation Tribunal decisions**
- They are searchable and name addresses, making them a small free lead source.
- VT00037229 confirms the premium carries over to a new owner.

**Session measurement:** your own sessions measured the over-banding cross-over as small (25 of 700 stuck estates; 3.6% against a 6.8% base). So F is a secondary lever.

All [verified]; `notes/eh_EF.md`.

---

## Corrections to the brief

- **Probate copy:** costs **£16**, not £1.50.
- **LP(MP)A 1994 s.17:** is about "absence of knowledge of intended recipient's death".
- **Premium exceptions:** the probate exception (Class I) applies from **1 April 2025**, not 2024.
- **Empty Property Hunters' backer:** The Harkalm Group, a property investment company, **not a PE firm**.
- **VAT:** the 2-year empties rate is Sch 7A **Group 7**, not Group 6.
- **CPR rule:** the rule for representing an estate with no personal representative is **19.12**, not 19.8.

## Not verified / blocked

- **Blocked:**
  - GRO death index coverage (the site returned 503).
  - Legacy.com UK (403).
  - PQ 24953 table (blocked).
  - Powys trading standards pages (403).
- **Found by search only [claimed]:** about 10 of the s.215 councils, and several operator claims (Property Filter users, PropMarker launch, OccupID).
- **Not found:**
  - Class F counts by duration.
  - Any national count of estates never administered.
  - Death-to-sale data.
  - TOLATA s.14 counts.
