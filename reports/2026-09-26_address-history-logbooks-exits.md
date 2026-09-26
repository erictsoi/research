# UK addresses, property logbooks and exit comparables — research report

**Date:** 26 September 2026
**Scope:** United Kingdom (England & Wales unless stated)

## Method and confidence tags

| Tag | Meaning |
|---|---|
| **[verified: primary]** | I read the primary page, statute, filing or dataset myself in this session. Key wording is quoted. |
| **[secondary]** | A secondary source (press, trade, company blog, third-party data site). "Search extract only" means the page was not opened. |
| **[inferred]** | My own reasoning or arithmetic. The working is shown. |
| **(blocked: host, code)** | The source could not be reached. This is recorded against the claim it affects. |

**Hosts that stayed blocked:**
- 403: commonslibrary.parliament.uk, researchbriefings.files.parliament.uk, hansard.parliament.uk, publications.parliament.uk, questions-statements.parliament.uk, ifs.org.uk, lyonsinquiry.org.uk, ofcom.org.uk, github.com, bidstats.uk, medium.com, en.powys.gov.uk, estateagenttoday.co.uk, www.costargroup.com, investors.costargroup.com, provequity.com, insidermedia.com.
- 405: webarchive.nationalarchives.gov.uk (AWS bot check).
- Connection resets: web.archive.org.
- Egress-blocked: whatdotheyknow.com, ukauthority.com, environment.data.gov.uk.
- Paywalled: realdeals.eu.com, primeresi.com.
- **Workaround:** historic Hansard was read through api.parliament.uk/historic-hansard.

**⚠ Corrections to the brief's premises** are flagged where they occur. In summary:
- The 1991 banding was mostly desk-based, not "drive-by".
- AddressBase launched in 2011, not 2012.
- "The PAF sale was a mistake" was said by a Commons select committee (PASC), not by ODUG.
- The NTSELAT material information guidance was withdrawn in May 2025.
- Landmark was not sold to Astorg.
- The "PropertyData" and "LandInsight" deals found online concern Australian firms, not the UK ones.
- The Residential Logbook Association's site is rlba.org.uk.

---

# PART A — Why UK addresses are still a mess

## 1. How council tax bands were set in 1991

### 1.1 Legal basis

**Valuation date.** LGFA 1992 s.21(2): "The valuations shall be carried out by reference to 1st April 1991". https://www.legislation.gov.uk/ukpga/1992/14/section/21/enacted **[verified: primary]**
- SI 1992/550 reg 6(1) (as made) defines value as what the dwelling "might reasonably have been expected to realise if it had been sold in the open market by a willing vendor on 1st April 1991".
- It assumes vacant possession, freehold (or a 99-year lease at a nominal rent for flats) and "reasonable repair". https://www.legislation.gov.uk/uksi/1992/550/regulation/6/made **[verified: primary]**

**Private valuers.** s.21(3): "the Commissioners of Inland Revenue may appoint persons who are not in the service of the Crown to assist them in carrying out the valuations". **[verified: primary]**

**Timetable.** s.22(2): the list "must be compiled on 1st April 1993".
- s.22(3): the listing officer "must take such steps as are reasonably practicable **in the time available** to ensure that it is accurately compiled".
- s.22(5): draft lists were due by 1 September 1992 and 1 December 1992.
- https://www.legislation.gov.uk/ukpga/1992/14/section/22/enacted **[verified: primary]**

### 1.2 Method — ⚠ mostly desk-based, not "drive-by"

The VOA Council Tax Manual, Section 1, Part 2, "the initial banding exercise" (updated 26 February 2025) describes it. https://www.gov.uk/guidance/council-tax-manual/section-1-introduction-and-essential-background **[verified: primary]**
- Para 2.1: "The initial banding exercise was carried out in 1991/1992. The Valuation Office Agency was responsible for the completion of the exercise and was assisted in its task by outside contractors."
- Para 2.2: "The Model sought to utilise to the full, information and records already held by the VOA to allow most dwellings to be banded **at the desk**. **Very few properties were externally inspected.** … key properties were identified, fully described and valued. This provided a basis for the banding of other properties by using comparables … **The Model was not appropriate for every locality or for the valuation of every dwelling in each locality.**"
- Para 2.3: sales evidence "within about 6 months of the AVD [antecedent valuation date] was analysed" for key properties.

**What this means.** The official account is that most homes were banded at a desk from existing rating-era records, by comparison with key ("beacon") properties. The popular "drive-by" story appears only in secondary sources and in the opposition's descriptions below. **[inferred]**

**Contractors barred from appeals.** Their contract said they would not "represent any taxpayer on any appeal … arising from any valuation banding(s) conducted by him". CTM Section 3, para 1.7: https://www.gov.uk/guidance/council-tax-manual/section-3-england-proposals-and-appeals **[verified: primary]**

### 1.3 What ministers said (Hansard, via api.parliament.uk/historic-hansard) **[verified: primary]**

- **Michael Portillo (Minister of State, DoE), HC Deb 12 June 1991, vol 192, c.929:** "It will not necessitate detailed knowledge of every property but will be much more broad-brush that [sic] the old rating system. **Many properties will not have to be inspected because they will clearly fall into one band or another.**" https://api.parliament.uk/historic-hansard/commons/1991/jun/12/valuation-of-domestic-properties
- **Baroness Blatch, HL Deb 20 June 1991, vol 530, cc.271–272:**
  - "there will be no need for precise valuations of every dwelling"
  - "we provisionally estimate that the banding task can be carried out for a sum of **£250 million—£11 for each property**"
  - the private sector would be used "where there is great expertise"
  - https://api.parliament.uk/historic-hansard/lords/1991/jun/20/local-government-finance-and-valuation
- **Portillo, HC Deb 16 December 1991, vol 201, cc.111–112:** "It will not be broad-brush. It will take account of local factors". This contradicts his June "much more broad-brush". **[inferred]** https://api.parliament.uk/historic-hansard/commons/1991/dec/16/valuation-bands
  - In the same debate (c.93), David Blunkett for the opposition described valuers "looking only at the front of a property as the valuer passes in his car". **This is an opposition characterisation.**
- **Lord Strathclyde, HL Deb 21 January 1992, vol 534, c.756:** "We now expect the valuation exercise to cost **£100 million less** than our original estimate … **The cost of £19 million to value about 12 million properties in England and Wales**". https://api.parliament.uk/historic-hansard/lords/1992/jan/21/local-government-finance-bill
  - Reading "about 12 million" as the share done by private contractors is **[inferred]**.
  - In the same debate (c.786), Baroness Hollis for the opposition reported that valuers would make "not even street-by-street inspections by car. Many valuers will gaze at a photograph". **Opposition characterisation.**
- **Robin Squire (Parliamentary Under-Secretary), HC Deb 24 June 1992, vol 210, c.270:** banding obviated "the need for precise valuations. With no attempt at such precision, the likelihood of disputes and appeals is greatly reduced." https://api.parliament.uk/historic-hansard/commons/1992/jun/24/local-government-finance
  - In the same debate (c.280), Eric Pickles, a backbencher, said "only 1 per cent. of firms performing those valuations were dismissed for repeated inaccuracies … the valuations of only 6.3 per cent. of properties were rejected as being inaccurate". **[verified: primary that he said it; the figures are not corroborated from any official source]**

### 1.4 Scale, staffing, cost and first-year fallout

**Dwellings banded.** Valuation Office Annual Report 1993–94 (OCR of scanned PDF): "by 31 March 1993 the Agency had ascribed **some 21 million dwellings** in England and Wales to one of 8 valuation bands". https://assets.publishing.service.gov.uk/media/5a7b99da40f0b645ba3c55f1/0539.pdf **[verified: primary]**

**First-year challenges.** The same report records:
- "**914,196** 'initial' proposals were actually received" in the 8 months to 30 November 1993, against a forecast of "up to 1 million";
- "631,216 bandings were reviewed against an expectation of 300,000";
- response targets were missed: 39% within 60 days and 54% within 90 days.

**[verified: primary]**

**Staffing.** There are **no banding-specific staff or contractor counts in official sources I could read.** **[verified: primary for the agency-wide figures]**
- Agency-wide, average employees were **5,851** in 1992–93 and **6,061** in 1993–94.
- In 1993–94, "Overtime, casual and fixed term appointments accounted for 1477 staff years".

**The key missing source.** The NAO's *Council Tax Valuations in England and Wales* (HC 1993-94 320, 8 April 1994) was a value-for-money study of the initial banding.
- NAO landing page: https://www.nao.org.uk/reports/council-tax-valuations-in-england-and-wales-2/ **[verified: primary]**
- The full text is only on the National Archives web archive (blocked: webarchive.nationalarchives.gov.uk, 405).

**Final total cost:** not found.

### 1.5 Challenges and changes since 1993

Source: VOA *Council Tax: challenges and changes, March 2024* (published 29 August 2024), the latest in the series. The 2026 stock release says list-change figures "will be produced at a later date" because of the new system.
- https://www.gov.uk/government/statistics/council-tax-challenges-and-changes-in-england-and-wales-march-2024/council-tax-challenges-and-changes-statistical-summary
- Time series: https://assets.publishing.service.gov.uk/media/66c75d1b07733cc4df618225/ct-cac-time-series-tables-2023-24.xlsx
- **[verified: primary]**

**2023–24:**
- "The number of received challenges in 2023 to 2024 was 43,820".
- Of resolved challenges, "27% resulted in a reduction".
- "4,960 (41%) of resolved band reviews resulted in a reduction".

**Cumulative, 1993–94 to 2023–24, England & Wales:**
- **2,832,920** challenges received.
- **1,308,620** resolved with the band decreased, about **46%** of resolved challenges.
- That is roughly **6%** of the original ~21m stock.
- These are my sums of tables CTCAC3.1 and 3.2. **[inferred from primary]**
- Caveats: figures are rounded to 10, the definition of a "challenge" changed in 2008, and I could not check for double-counting of proposals and appeals.

### 1.6 Official admissions of limits

- **VOA manual:** "Very few properties were externally inspected"; "The Model was not appropriate for every locality". **[verified: primary]**
- **Statute:** "reasonably practicable in the time available" (s.22(3)). **[verified: primary]**
- **Lyons Inquiry final report, *Place-shaping* (March 2007).** https://assets.publishing.service.gov.uk/media/5a7c093540f0b645ba3c64cb/9780119898545.pdf **[verified: primary]**
  - Para 7.43: "up to 11 million households would have been expected to move to a different council tax band (around half of all households in England)".
  - Para 7.44: "3.7 million households (or 17 per cent of all households in England) … are arguably paying too much council tax".
  - Para 7.50: "an out of date tax base will mean that the credibility of council tax as a property tax will gradually be eroded".
  - Para 7.59: the VOA advised "it would be difficult to re-band properties consistently in areas whose relative desirability had radically altered since 1991".
  - Box, p.235: "fewer than one per cent of all homeowners are visited by VOA staff each year".
  - **The phrase "rough and ready" does not appear in the Lyons final report or annexes** (text searched). Its 2005 interim papers could not be reached (lyonsinquiry.org.uk, 403).
- **Could not reach:**
  - Commons Library briefings (blocked: commonslibrary, 403).
  - IFS revaluation reports (blocked: ifs.org.uk, 403).
  - A 1994 PAC report was not found.

### 1.7 Wales and Scotland

- **Scotland:** local assessors did the valuation, "acting under the direction of the Commissioners" (CTM Practice Note 1). **[verified: primary]**
- **Wales revaluation (list in force 1 April 2005, valuation date 1 April 2003).** CTM para 2.5 says it was "manual" and "followed closely the approach adopted for the 1993 Initial Banding Exercise". Unlike 1991, it used "taxpayer questionnaires together with external and internal inspections". **[verified: primary]**
- **Wales outcome:** 438,760 properties (33%) moved up a band and 105,380 (8%) moved down, out of 1,317,450. Source: Hincks & Leishman, UK Collaborative Centre for Housing Evidence, 2021, https://housingevidence.ac.uk/wp-content/uploads/2025/02/Revaluation-of-council-tax-in-Wales-Final-version-February-2021.pdf **[secondary]**

## 2. The UPRN, GeoPlace and AddressBase

### 2.1 BS 7666

**Editions:**
- BS 7666 "has been through a number of revisions since its inception in 1994" (NLPG explainer, https://www.esdm.co.uk/Data/Sites/1/media/software/cams/services/BS7666_Explained.pdf). **[verified: primary — NLPG document, not BSI]**
- BSI records **[verified: primary]**:
  - BS 7666-1:2006 "Supersedes BS 7666-1:2000 and BS 7666-4:2002". https://www.thenbs.com/PublicationIndex/documents/details?Pub=BSI&DocID=279575
  - BS 7666-0:2006 "supersedes BS 7666-3:2000" (published 28 July 2006).
  - BS 7666-2:2020 (published 31 December 2020) "enables different users of land and property information to link … via a common unique property reference number (UPRN)". https://knowledge.bsigroup.com/products/spatial-datasets-for-geographical-referencing-specification-for-a-land-and-property-gazetteer-1
- The Open National Address Gazetteer report (below) says "The data structure of the NAG data is based on the British Standard BS7666:2006". **[verified: primary]**
- Which parts existed in 1994 is unverified.

### 2.2 NLPG origins

**GeoPlace press release, 2008** (https://www.geoplace.co.uk/press/2008/commercial-launch-of-nlpg-nationwide-property-identification-system-announced) **[verified: primary]**:
- "The NLPG was initiated in **1999** to become the master address dataset for England and Wales".
- It was boosted in 2005 by the Mapping Services Agreement, brokered by IDeA with **Intelligent Addressing** through its subsidiary LGIH.
- The commercial launch was on 30 April 2008.

**BIS/Katalysis, *An Open National Address Gazetteer* (BIS/14/513, January 2014)** (https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/274979/bis-14-513-open-national-address-gazetteer.pdf) **[verified: primary]**:
- Ordnance Survey (OS), local government and others "were not able to agree … local government alone developed the NLPG as an essentially competing product to PAF/ADDRESS-POINT".
- It describes a "fifteen year" period of "unproductive discord".
- **Scotland:** the One Scotland Gazetteer is "essentially the same in terms of principles", funded through the Improvement Service.
- **Northern Ireland:** Pointer, maintained by Land & Property Services, "has been allocated a set of UPRNs from the NLPG national hub".

### 2.3 GeoPlace

- **Announced 3 December 2010** as a joint venture between OS and the Local Government Group; the NAG would be "free to all public services". https://www.gov.uk/government/news/new-national-address-book-to-be-free-to-emergency-services **[verified: primary]**
- **Incorporated 17 November 2010** as GeoPlace LLP (OC359627). https://find-and-update.company-information.service.gov.uk/company/OC359627 **[verified: primary]**
- **Formed 31 March 2011** after OFT approval, "jointly owned by the Local Government Group and Ordnance Survey". It "started our work in 2011". https://www.geoplace.co.uk/press/2011/geoplace-announces-plans-for-the-national-address-gazetteer-database **[verified: primary]**
- **Bought Intelligent Addressing in 2011:** "IA was purchased by GeoPlace in 2011 … In its last year of trading (2010), IA had a cost of £2.7m and 30 staff" (BIS 2014). **[verified: primary]**

**⚠ Ownership: "50/50" is true for control, not necessarily for profit.**
- The board has "two members from the LGA and two from Ordnance Survey". https://www.geoplace.co.uk/about-us/our-people/the-board **[verified: primary]**
- Companies House shows each member (Ordnance Survey Ltd; Improvement and Development Agency for Local Government) holding "More than 25% but not more than 50%" of voting rights and surplus assets. **[verified: primary]**
- But BIS 2014 says: "Currently, the profit is divided between OS and LGA in a **75:25 ratio**, reflecting initial investment inputs." **[verified: primary]**
- No current source on the profit split was found.

**What it does.** GeoPlace works "contractually with all 339 councils in England and Wales" and updates "around 2 million records" a month. https://www.geoplace.co.uk/about-us/who-we-are/our-work **[verified: primary]**

### 2.4 AddressBase products — ⚠ launched 2011, not 2012

- **Launch, 30 September 2011:** "AddressBase, AddressBase Plus and AddressBase Premium are available from 12 noon on Friday 30 September". They were sold under the PSMA and "through commercial licences to other sectors". https://www.geoplace.co.uk/press/2011/new-addressing-products-now-available-from-ordnance-survey **[verified: primary]**
- **Scotland** was added in May 2012. https://www.geoplace.co.uk/press/2012/scottish-addresses-added-to-addressbase-products **[verified: primary]**
- **AddressBase Core** was released in July 2020 (OS AddressBase Product Overview v3.2). **[verified: primary — OS document hosted by a reseller]**
- **2014 pricing:** £189,370 a year for national, full-specification AddressBase (101+ terminals). GeoPlace net revenue was £9.5m in 2011/12 (BIS 2014). **[verified: primary]**
- **End of life:** "AddressBase and AddressBase Plus will reach their end of life in **Autumn 2027**". They are replaced by **OS GB Address** ("updated daily") and OS Islands Address. https://www.ordnancesurvey.co.uk/products/addressbase **[verified: primary]**
  - AddressBase Premium and AddressBase Core are still listed as "In-life" products, with no end date given. **[verified: primary]**

#### 2.4a What AddressBase is, and what replaces it (OS GB Address)

**In plain terms.** AddressBase is Ordnance Survey's licensed national address file. Every UPRN comes with its full address text, coordinates and a classification (house, flat, shop and so on). Its sources are the council gazetteers (via GeoPlace), OS mapping and Royal Mail's PAF. The free OS Open UPRN (2.6) gives only the number and coordinates. **[inferred from the sources in 2.4–2.6]**

**The replacement.** OS GB Address is "A complete and authoritative addressing dataset for Great Britain, providing a detailed view of an address and its lifecycle, based on pre-build, built, and historical property lifecycle phases. This product is updated daily". It is "generated from the National Geographic Database" (NGD). https://www.ordnancesurvey.co.uk/products/os-gb-address **[verified: primary]**
- The NGD Address theme "contains all of the address data found in the OS AddressBase Premium product". https://docs.os.uk/osngd/data-structure/address **[verified: primary]**
- Northern Ireland, the Isle of Man and the Channel Islands are covered by a sister product, OS Islands Address. **[verified: primary]**

**What it contains** (OS NGD documentation; https://docs.os.uk/osngd/data-structure/address/gb-address/built-address) **[verified: primary]**
- **Six feature types:** Built Address, Pre-Build Address, Historic Address, Non-Addressable Object, Street Address and Royal Mail Address. Each is a separate table, so planned, live and demolished addresses are distinguished.
- **Built Address** is defined as "local authority addresses that are currently built and live and can typically receive mail, deliveries, or services".
  - Schema v1.0 launched 2 November 2022, v2.0 on 28 March 2023 and v3.0 on 30 September 2025.
- **Built Address attributes include:**
  - `uprn`, `parentuprn`, `rootuprn` and `hierarchylevel` (so flats link to their building);
  - `usrn` (the street);
  - `fulladdress`, plus Welsh and Gaelic alternate-language versions;
  - `floorlevel`, `lowestfloorlevel` and `highestfloorlevel`;
  - a four-level classification (`primary` to `quaternaryclassificationdescription`);
  - `buildstatus`, `buildstatusdate` and `addressstatus`;
  - `lowertierlocalauthoritygsscode`;
  - `positionalaccuracy`, `effectivestartdate` and `effectiveenddate`.
- **Versioning:** each feature carries its own version dates, and past snapshots can be requested ("temporal filtering").
- **Royal Mail Address** holds PAF delivery points (`udprn`) matched to UPRNs.
  - It records match type, match method and "unmatched reason".
  - Schema v2.0, due "early October 2026", adds "Full NYB content" (Not Yet Built) and "Full MR content" (Multiple Residence). https://docs.os.uk/osngd/data-structure/address/gb-address/royal-mail-address
- **Cross-references:** the Related Entity component "provides cross-reference information to key identifiers from other datasets, allowing for the UPRN … to be linked to them". https://docs.os.uk/osngd/data-structure/address/address-related-components/related-entity
  - Its code list (v2.0, 30 September 2025) includes **"VOA Council Tax — Valuation Office Agency (VOA) Council Tax Assessment Unique Address Reference Number (UARN)"** and **"VOA Non Domestic Rates"**.
  - It also links OS Building Part, Land, Road Link, Ward and Parish features. https://docs.os.uk/osngd/code-lists/code-lists-overview/dataentitycatalogue
  - So a licensed user can join a UPRN to the VOA's council tax record reference. **The band itself is not supplied** (no band attribute appears in the schemas read). **[verified: primary; absence of a band field checked in the Built Address schema]**
- **Formats and access:** CSV or GeoPackage, downloaded from the OS Data Hub through OS Select+Build. It is not offered through the Features or Tiles APIs. **[verified: primary]**

**What is better than AddressBase / AddressBase Plus** **[inferred from the above]**
1. Updates are daily rather than periodic epochs.
2. The lifecycle is explicit: pre-build, live and historic addresses are held separately, with dates.
3. Floor levels and a parent/root UPRN hierarchy for flats and multi-occupancy buildings.
4. Links to OS buildings, land use and VOA UARNs in one linked database.
5. PAF matching is transparent, including why a delivery point did not match.

**Unchanged:** it is still a **licensed** product, and the address text still carries Royal Mail PAF terms. No OS GB Address prices were found on OS pages. Access for public-sector bodies under the PSGA is **[inferred]**, not confirmed on the product page.

### 2.5 Licensing history

- **PSMA (England & Wales):** "will come into effect from 1 April 2011 … centrally-funded by CLG" (DCLG PSMA Transition Plan, August 2010). https://assets.publishing.service.gov.uk/media/5a79c8e5e5274a684690c165/1665146.pdf **[verified: primary]**
  - That it was a 10-year deal is **[secondary]**.
- **One Scotland Mapping Agreement:** "preceded the PSMA" (BIS 2014). **[verified: primary]** Start date not verified.
- **PSGA, from 1 April 2020** ("will start from 1 April 2020"; titled "new 10 year"). https://www.gov.uk/government/news/government-announces-new-10-year-public-sector-geospatial-agreement-with-ordnance-survey **[verified: primary]**
  - Contracts Finder: awarded 31 March 2020; runs **1 April 2020 – 31 March 2030**; "Total value of contract **£962,939,000**"; buyer Cabinet Office (Geospatial Commission). https://www.contractsfinder.service.gov.uk/notice/d521990b-993a-40a2-a9f8-92332a105e4a **[verified: primary]**
  - Scope: "Any public sector organisations ranging from health and emergency services, town, parish, and community councils through to central government departments can sign up". Membership was 5,836 organisations in 2021/22; OS now says "more than 6,000". **[verified: primary]**
- **PAF Public Sector Licence:**
  - 2020–23: started April 2020. It was reportedly worth £15.75m **[secondary; blocked: bidstats.uk, 403]**.
  - **2023–28:** "a new 5 year arrangement … until 31 March 2028", value **£30,800,000**, "usage is free at the point of use". https://www.contractsfinder.service.gov.uk/notice/2ade58bd-a604-4368-a1cf-a680284f40c3 **[verified: primary]**

### 2.6 OS Open UPRN and Open USRN (July 2020): what is free and what is paid

- **Announced 2 April 2020:** identifiers "will be made available as open data under the Open Government Licence (OGL) from July 2020". https://mhclgdigital.blog.gov.uk/2020/04/02/unique-property-identifiers-to-be-opened-under-open-government-license/ **[verified: primary]**
- **Released 1 July 2020:** UPRNs and USRNs "will be the standard for central government and NHS organisations … now openly available and royalty free". https://www.geoplace.co.uk/press/2020/central-government-and-the-nhs-must-now-use-uprns-and-usrns-to-unlock-the-power-of-place **[verified: primary]**
- **What is free:**
  - OS Open UPRN has only "UPRN, X_COORDINATE, Y_COORDINATE, LATITUDE and LONGITUDE". **There is no address text.**
  - It is refreshed every six weeks; the latest release is September 2026 (Epoch 130).
  - It covers about 40 million addressable locations.
  - https://docs.os.uk/os-downloads/products/addresses-and-names-portfolio/os-open-uprn/os-open-uprn-overview **[verified: primary]**
  - OS Open USRN (simplified line geometry), Open TOID and Open Linked Identifiers are also free under OGL. https://www.ordnancesurvey.co.uk/products/open-mastermap-programme/open-id-policy **[verified: primary]**
- **The policy bans reverse-engineering the address.** It forbids, for example, making available "UPRNs with a building number of 1 … as this would enable reverse engineering of a premium attribute (i.e. the house number)". **[verified: primary]**
- **What is still paid:**
  - The address text is in AddressBase, which "Contains Local Authority, Ordnance Survey and Royal Mail addresses".
  - OS must "pass on" Royal Mail's PAF terms: "As all of our addressing products … contain Royal Mail's Postcode Address File (PAF®) data". https://www.ordnancesurvey.co.uk/licensing/paf-licence **[verified: primary]**
- **The mandate:**
  - In 2015 the Open Standards Board decided "the UPRN should not be adopted as an open standard because of licensing restrictions". https://technology.blog.gov.uk/2020/04/02/identifying-properties-and-streets-in-government-data **[verified: primary]**
  - The standard *Identifying property and street information* was first published **1 July 2020** and updated 29 January 2026. It says: "Systems, services and applications that store or publish data sets containing property and street information **must use the UPRN and USRN identifiers**." https://www.gov.uk/government/publications/open-standards-for-government/identifying-property-and-street-information **[verified: primary — current version only]**
  - CDDO guidance (28 July 2021): "All public sector bodies should use AddressBase Core for accessing address data rather than paying for other third party products." https://www.gov.uk/guidance/access-free-address-data-using-addressbase **[verified: primary]**

## 3. Royal Mail PAF and the open-address-register debate

### 3.1 Legal duty and ownership

**Legal duty.** Postal Services Act 2000 s.116(1): the owner of the PAF "shall— (a) maintain the File, and (b) make the File available to any person who wishes to use it on such terms as are reasonable". https://www.legislation.gov.uk/ukpga/2000/26/section/116 **[verified: primary]**
- Since 1 October 2011, Ofcom may direct the terms (s.116(5)–(6), inserted by the Postal Services Act 2011).

**Privatisation (2013).** "The Postal Address File had remained an asset of Royal Mail at privatisation" (Public Sector Transparency Board minutes, 11 June 2014). https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/501886/Minutes_to_the_Public_Sector_Transparency_Board_meeting_11_06_2014.pdf **[verified: primary]**

**Ownership today: EP Group and J&T Capital Partners.**
- The National Security and Investment Act final order came into force on 19 December 2024. https://www.gov.uk/government/publications/acquisition-of-international-distribution-services-plc-by-ep-uk-bidco-limited-notice-of-final-order/acquisition-of-international-distribution-services-plc-by-ep-uk-bidco-limited-notice-of-final-order **[verified: primary]**
- The EP UK Bidco offer for International Distribution Services plc was declared unconditional on **30 April 2025** (about 80.06% of shares). Bidco is "owned indirectly by (i) EP Group, a.s. … and (ii) J&T Capital Partners, a.s.". https://www.investegate.co.uk/announcement/rns/international-distributions-services--ids/offer-declared-unconditional/8855237 **[verified: primary]**
- Acceptances then reached 90.15%, followed by compulsory acquisition (RNS of 28 May 2025). **[verified: primary]**
- Daniel Křetínský's personal control of EP Group is **[secondary]**.

### 3.2 Regulation and licence costs

**Ofcom review.**
- Ofcom's last full PAF review was in 2013: consultation on 7 February 2013, statement in July 2013 (as quoted in BIS 2014). **[verified: primary]**
- Ofcom's own documents could not be read (blocked: ofcom.org.uk, 403).
- Centre for Public Data (2021): "the last time it did so was in 2013". https://www.centreforpublicdata.org/ask-ofcom-to-review-address-data **[verified: primary — campaign group]**

**PAF economics (2011/12):** revenue £27.1m, cost £24.5m (BIS 2014, citing regulatory accounts). **[verified: primary]**

**Current solutions-provider licence prices** (excluding VAT) **[verified: primary]**:
- User £105; Transactions £1.82 per block of 100; Website £7,525; Organisation £22,600.
- https://www.poweredbypaf.com/pricing-solutions-provider/

**New prices from 1 October 2026** ("Our PAF Licence & Supply prices are changing with effect from 1 October 2026") **[verified: primary]**:
- User £115; Transactions £1.94; Website £8,210; Organisation £25,000; Corporate £200,000 (was £180,000).
- https://www.poweredbypaf.com/wp-content/uploads/2026/08/2026-Pricing-Factsheet.pdf

**Free tiers** **[verified: primary]** https://www.poweredbypaf.com/pricing/:
- Charities and community interest companies with income "less than £10million" may get free PAF for non-commercial use.
- Microbusinesses get it free for one year.
- Public sector: free at the point of use under the Public Sector Licence.

### 3.3 The open-address-register debate

- **ODUG case, November 2012.** The Open Data User Group (ODUG) "presented the Data Strategy Board (DSB) with a case for the release of a free national address database" (BIS 2014). **[verified: primary]**
  - Katalysis recommended that "a basic address product should be free to all users at the point of use under the Open Government Licence". It estimated compensation at "almost £40m per year … some £27m for RM and £10m for GeoPlace".
- **⚠ "A mistake" was PASC, not ODUG.** The Commons Public Administration Select Committee (*Statistics and Open Data*, HC 564, 2013–14) called selling the PAF with Royal Mail a "mistake". It also said "Public access to public sector data must never be sold or given away again".
  - I read this as reproduced by ODUG, which wrote "ODUG agrees fully with the conclusion of the HoC PASC Report". https://data.blog.gov.uk/2014/04/28/odug-response-to-paf-advisory-board-response/ **[verified: primary for ODUG's text; secondary for PASC's words]**
  - PASC's own report could not be read (blocked: publications.parliament.uk, 403).
  - ODUG also called Royal Mail's "annual £24.5 million of cost" for PAF "excessive, unreasonable and unfair". **[verified: primary — ODUG view]**
- **ODI Open Addresses UK.** A £383k Release of Data Fund grant: https://www.theodi.org/article/383k-government-grant-released-to-create-uk-open-address-list/ **[verified: primary]**
  - The Transparency Board approved stages of £28,800, then £132,000, then £250,800. £132,000 + £250,800 = £382,800 **[inferred]**.
  - The alpha launched in January 2015. The project was later "hibernated" (Boswarva primer) **[secondary]**.
  - **Date conflict:** the ODI page is dated April 2014, but the funding was approved in June 2014.
- **Budget 2016, para 2.324:** "The government will provide up to £5 million to develop options for an authoritative address register that is open and freely available." https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/508193/HMT_Budget_2016_Web_Accessible.pdf **[verified: primary]**
  - Outcome: "unclear how or if that money was spent. An incipient GDS attempt to build an address register was abandoned in 2017" (Boswarva). **[secondary]**
- **Geospatial Commission since 2018:** PSGA (2020), opening UPRN and USRN (2020), and the PAF Public Sector Licence renewal (2023–28). **No policy for an open address register with address text was found** in the UK Geospatial Strategy 2030. **[verified: primary for its contents; absence inferred]**
- **ONS Address Index** matches addresses to UPRNs against AddressBase (ONS Working Paper 17). The Census 2021 address frame used AddressBase Premium epoch 77 (June 2020). **[verified: primary]**

### 3.4 Is there an official estimate of what poor address data costs? — No

**No official government estimate of the cost of poor addressing was found.** The figures in circulation are value or return-on-investment studies commissioned by interested parties:
- **PAF Advisory Board (2012):** PAF's economic *value* is "between £992m-£1.38bn per annum" (quoted in BIS 2014). **[verified: primary quote; the PAB is a Royal Mail users' board]**
- **GeoPlace/ConsultingWhere (2016):** "net benefits up to £202 million by 2020 … 4:1" ROI. https://www.geoplace.co.uk/case-studies/geoplace-identifies-4-1-roi **[verified: primary — commissioned]**
- **GeoPlace/ConsultingWhere (August 2022):** councils "realised increased revenue and cost savings of an estimated £250 million over the last 5 years". https://www.geoplace.co.uk/addresses-streets/location-data/value-of-data/reports **[verified: primary — commissioned]**
- **BIS/Katalysis (2014):** opening addresses would add "£13.2m - £30.4m increase in GDP in 2016". **[verified: primary — official commissioned report; this is the benefit of opening, not the cost of poor data]**
- **Do not confuse:** the Geospatial Commission's £2.4bn a year figure is for underground utility strikes, not addressing. **[verified: primary]**

## 4. The VOA council tax list and UPRNs

### 4.1 Does the list carry UPRNs? Not natively

- **Statutory contents.** The list holds "the reference number ascribed to the dwelling by the listing officer" (SI 1992/553 reg 2, as made). No UPRN is required. https://www.legislation.gov.uk/uksi/1992/553/made **[verified: primary; later amendments not checked]**
- **Linking is done by GeoPlace, and it is imperfect.** ONS quality assurance note (2020) **[verified: primary]** https://www.ons.gov.uk/peoplepopulationandcommunity/housing/methodologies/valuationofficeagencypropertyattributedataqualityassuranceofadministrativedatausedincensus2021:
  - "All dwellings from VOA data (UARNs) are mapped to UPRNs so that VOA references can be included in AddressBase products."
  - "For a minority of records, GeoPlace are unable to uniquely map UARNs to the lowest level (child) UPRN. In that case a group of UARNs are assigned to a higher level (parent) UPRN."
- **The data supplied to ONS has a UPRN field.** It includes "the National Land and Property Gazetteer Unique Property Reference Number (NLPG-UPRN …)". https://www.ons.gov.uk/census/censustransformationprogramme/administrativedatacensusproject/datasourceoverviews/valuationofficeagencydata **[verified: primary]**
- **Legacy systems.** UKAuthority reports that "The VOA's legacy systems have not accommodated UPRNs to date". **[secondary, search extract only; blocked: ukauthority.com; date unknown]**
- **New system.** The Valuation Office moved council tax onto "a new, modern operating system in 2025". No statement on native UPRN storage was found. **[verified: primary]**
- **Business rates.** The VOA holds a UARN–UPRN lookup but refused to publish it (FOI response published 4 September 2025, FOIA s.44(1)(a); Commissioners for Revenue and Customs Act 2005 ss.18, 23). https://www.gov.uk/government/publications/lookup-table-to-connect-all-publicly-available-uarn-to-the-uprn-system/response-for-a-lookup-table-for-uarn-and-uprn-data **[verified: primary]**

### 4.2 What the VOA publishes

- **Band-check service** (https://www.tax.service.gov.uk/check-council-tax-band/search) searches by postcode. Its footer credits OS and IDeA (i.e. AddressBase/NLPG) address data. **[verified: primary — search page]**
  - Whether results show a UPRN could not be checked (blocked: result page, 403).
- **Stock statistics:** aggregate tables by band, type, build period and bedrooms, down to LSOA. They are geocoded by postcode and billing authority code; the 2026 background document never mentions "UPRN". **[verified: primary]**
- **No bulk address-level list download was found.**

### 4.3 The VOA's own admissions that it lacks property details **[verified: primary]**

**Council Tax: stock of properties, 2026 — background information** (published 24 September 2026). https://www.gov.uk/government/statistics/council-tax-stock-of-properties-2026/background-information
- "**In April 1993, 35% of properties had an unknown property type, 2% of properties had an unknown number of bedrooms and 37% of properties had an unknown build period.**"
- "Since March 2014 … reduced to less than 1% in each category."
- "the Valuation Office cannot review the banding … until the property is sold … property details **may not reflect the current property details**."

**2026 commentary** **[verified: primary]**
- There were 27.4m properties on the list.
- 0.17m (0.6%) had an unknown property type and 0.13m (0.5%) an unknown number of bedrooms.
- Build period was "Unknown" for 202,450 properties (table CTSOP4.0).

**Property attribute data guidance** (https://www.gov.uk/guidance/property-attribute-data-pad) **[verified: primary]**
- "Property attribute data is historic. It usually relates to the state of a property on … 1 April 1993 in England".
- "Legally we cannot review improvements to a property until it is sold."

**UK HPI quality note** (updated 22 December 2023) **[verified: primary]**
- The VOA "only collect data that is needed to place an accurate band on the property".
- "Changes made to properties such as improvements are also difficult to capture".
- **Flag:** the same note reads "VOA does hold contemporary data for all dwellings", which appears to be a drafting error for "does not". Do not quote it without that caveat.

**Digitisation**
- Attributes were digitised from paper records in a "bulk capture exercise during 2003 and 2004 in England and during 2005 in Wales" (ONS). **[verified: primary]**
- ONS found 86% agreement between 2011 Census accommodation type and VOA property type. **[verified: primary]**

**The VOA's proposal form asks owners for these details** (Form VO 7455 (10/25), Part D). https://assets.publishing.service.gov.uk/media/68fb449fb3e33205c4e6f077/council_tax_proposal_form_england.pdf **[verified: primary]**
- "**Year property built: If unknown please estimate year here**".
- Numbers of reception rooms, bedrooms, bathrooms and kitchens.
- Garage, conservatory, central heating.
- Part E: extensions, loft conversions, and "who built the extension(s) including date of completion(s)".

**VOA merged into HMRC.** "On 1 April 2026, the work of the Valuation Office Agency (VOA) was brought into HM Revenue and Customs (HMRC), and the VOA has ceased to exist as an executive agency." https://www.gov.uk/government/news/valuation-office-joins-hm-revenue-and-customs **[verified: primary]**

## 5. Which public datasets carry UPRN, and since when

| Dataset | UPRN? | Since | Source / tag |
|---|---|---|---|
| **EPC register (England & Wales)** | Yes | "**November 2021** – UPRNs … were added to the data" | https://get-energy-performance-data.communities.gov.uk/guidance/changes-to-the-format-and-methodology **[verified: primary]**. The UPRN is OGL; address fields are restricted, being "processed against Ordnance Survey's Address Base Premium product, which incorporates Royal Mail's PAF®" (…/guidance/licensing-restrictions) **[verified: primary]** |
| **HMLR Price Paid Data** | **No UPRN column** | — | https://www.gov.uk/guidance/about-the-price-paid-data **[verified: primary]** |
| **HMLR Price Paid Transaction ID ↔ UPRN lookup** | Yes (separate table) | **First published 28 August 2026**; new records only ("will not provide back-dated data"); OGL; monthly | https://www.gov.uk/government/statistical-data-sets/transaction-unique-identifier-and-uprn-look-up-table-dataset **[verified: primary]** |
| **HMLR Title Number ↔ UPRN lookup** (National Polygon Service) | Yes | data.gov.uk record Dec 2020 | HMLR: "licensed, chargeable" (https://use-land-property-data.service.gov.uk/datasets/nps) **[verified: primary]**. **Conflict:** data.gov.uk lists OGL |
| **HMLR Registered Leases** | Yes | 28 July 2020 | https://www.gov.uk/government/news/hm-land-registry-backs-innovation-and-transparency-with-new-data-releases **[verified: primary]** |
| **VOA business rates lists** (2010/2017/2023/2026) | **No** (uses UARN; lookup refused under FOI, see 4.1) | — | Data specification has no "UPRN" field; restricted licence ("An open government licence does not apply") https://voaratinglists.blob.core.windows.net/html/rlidata.htm **[verified: primary]** |
| **ONS National Statistics UPRN Lookup (NSUL)** | Yes | By **January 2020** (AddressBase epoch 72) ⚠ earlier than the brief's "2021" | https://www.data.gov.uk/dataset/40584b1b-1836-4ec5-ab50-d3be563fc17c/national-statistics-uprn-lookup-january-2020 **[verified: primary]** |
| **planning.data.gov.uk** | Field present in planning-application, tree, educational-establishment, article-4 and listed-building datasets | Dates not verified; having the field does not mean it is filled in | Datasette schema query **[verified: primary]** |
| **DfE Get Information about Schools** | Yes (column "UPRN"); 39,844 of 52,572 records filled (my count, 26 Sep 2026 extract) | Seen by Oct 2023 **[secondary]** | edubasealldata20260926.csv **[verified: primary]** |
| **CQC** | Yes, in the HSCA Active Locations file ("Location UPRN ID"); not in the simple directory CSV | Not verified | https://www.cqc.org.uk/about-us/transparency/using-cqc-data **[verified: primary]** |
| **NHS ODS API** | Yes (`GeoLoc.Location.UPRN`) | Not verified | https://directory.spineservices.nhs.uk/ORD/2-0-0/organisations/RR8 **[verified: primary]** |
| **FSA food hygiene ratings** | **No** | — | https://api.ratings.food.gov.uk/establishments/1954128 **[verified: primary]** |
| Environment Agency flood data | Not verified | — | (blocked: environment.data.gov.uk) |

---

# PART B — Digital property logbooks and property data rules (June 2026 to today)

## 6. MHCLG Home Buying and Selling Reform Roadmap (June 2026)

**Publication.** Published **19 June 2026** as the outcome of two consultations, "home buying and selling reform; material information in property listings". https://www.gov.uk/government/consultations/home-buying-and-selling-reform/outcome/home-buying-and-selling-reform-roadmap **[verified: primary]**
- The consultations ran 6 October – 29 December 2025 and drew 1,133 and 188 responses. **[verified: primary]**
- Press release: https://www.gov.uk/government/news/homebuying-shake-up-to-slash-delays-cut-costs-and-stop-sales-falling-through **[verified: primary]**
  - It claims the reforms will "cut buying times by around four weeks, save first-time buyers an average of £650" and "halve the number of sales that fall through".
  - Its metadata says 18 June, but the text says "today (Friday 19 June)".
- The written statement HLWS134 (22 June 2026) could not be read (blocked: questions-statements.parliament.uk, 403).
- Coverage: "the majority of measures … will apply in England, Wales and Northern Ireland". **[verified: primary]**

**Timeline in the roadmap (quoted)** **[verified: primary]**

*"Now (in 2026)":*
- "publish non-statutory guidance to improve the quality of information in property listings"
- identify "sales pack" information "that can be voluntarily provided, upfront immediately"
- "publish a non-statutory Code of Practice setting out minimum standards for property agents"
- build preparedness for binding contracts and awareness of "the voluntary use of reservation agreements"
- "publish a call for evidence on a smart data scheme for the property sector"

*"Next (in 2027 to 2028)":*
- "facilitate uptake of digital ID, Qualified Electronic Signatures, and digital logbooks and packs"
- "create a voluntary accreditation scheme to identify data standards that meet a core set of criteria"
- "consult on a smart data scheme for the property sector"
- consult on mandatory qualifications for agents

*"Future (by end of Parliament)"*, "When parliamentary time allows, introduce legislation to":
- "require the preparation of 'sales packs' prior to listing, including searches and a property condition report"
- "require the use of binding conditional contracts … after sales packs are embedded"
- "make digital sales packs and logbooks a standard feature of all property transactions"

**No bill is named.** **[inferred from the text]**

**On digital logbooks (Chapter 6)** **[verified: primary]**
- "82% of responses … agreed that government should aim to support the wider use of digital property logbooks and packs."
- "we will legislate to make both digital property logbooks and sales packs a requirement for all property transactions when parliamentary time allows" and "mandate the minimum, standardised data that both products should contain".

**On upfront information (Annex B)** **[verified: primary]**
- The expected sales pack contents include tenure, **Council Tax Band**, EPC rating, title information, searches, a property questionnaire, a condition report and a floor plan.
- The annex adds: "Specific details are subject to change".

**On data standards (Chapter 10)** **[verified: primary]**
- A future regulatory framework "to store, maintain and share data in a secure way … rules on liability and consumer protection".
- A voluntary accreditation scheme "next year".
- £1.4m for local-authority data standards.
- "complete the Local Land Charges programme by 2028".
- A "fully digital, geospatial title (land) register by 2035".

**⚠ UPRN and BASPI are absent from the roadmap** (text searched). **[verified: primary]**
- By contrast, the October 2025 consultation proposed "a standardised core data set for all digital packs, **linked to the Unique Property Reference Number (UPRN)** and Land Registry records". https://www.gov.uk/government/consultations/home-buying-and-selling-reform/home-buying-and-selling-reform **[verified: primary]**

**Delivery since June.** No published Code of Practice or listing guidance was found as of 26 September 2026. **[secondary: search only]**

## 7. HM Land Registry logbook proof of concept

- **What it is.** RLBA, "June 2026 - HMLR and RLBA Begin Logbook Integration Trial": "homeowners will be able to see HMLR Register Extract Service data directly in their Digital Property Logbooks". https://www.rlba.org.uk/news **[verified: primary]**
- **Duration and scale.** "a **12-month** digital property logbook trial set to begin this month". "**Four** RLBA‑registered logbook providers are expected to take part, with estimated requests for register data expected to reach up to **2,500**." Today's Conveyancer, 3 June 2026: https://todaysconveyancer.co.uk/homeowners-given-access-hmlr-data-digital-property-logbook-trial/ **[secondary]**
  - **The four providers are not named in any source found.**
- **What data.** Title register data via API. Homeowners "won't be able to use the data to transact, but will be able to use it to create Digital Sales Pack in their Logbook. Official Copies … will still need to be purchased". Access is gated by the National Logbook Register verifying the owner. **[verified: primary — RLBA]**
- **Official references.**
  - The roadmap cites "the Residential Logbook Association's proof of concept project testing how HM Land Registry (HMLR) data can be accessed within logbooks". **[verified: primary]**
  - The HMLR Business Plan 2026 (31 March 2026) promises "proof‑of‑concept activity, including … digital property logbooks". https://www.gov.uk/government/publications/hm-land-registry-business-plan-2026/hm-land-registry-business-plan-2026 **[verified: primary]**
  - **Conflict:** the Business Plan says local land charges migration will be complete "By April 2029", while the roadmap says "by 2028".
  - No HMLR blog post about the trial was found.

## 8. Residential Logbook Association (RLBA)

- **Identity.** The domain is **rlba.org.uk**. It describes itself as "the MHCLG supported trade association and self-regulatory body for companies providing digital logbooks". It is a company limited by guarantee "run by its members on a voluntary basis". https://www.rlba.org.uk/about ; https://www.rlba.org.uk/membership **[verified: primary]**
- **Members** (from the logos on the /about page; that all are current is **[inferred]**) **[verified: primary]**:
  - Chimni, Data Door, NDD, HOP (Homeowners Passport), Block Manager, DataPal, GBuilder, HomeHogs, Novoville, Shedyt and AHMS.
  - February 2025 news: eight organisations and "around half a million" compliant logbooks.
  - **Moverly is not a member.** It appears only as an early Register API user in 2023.
- **Standard.** "The RLBA's Core Logbook standard was agreed with MHCLG in 2020 and has been updated variously since." No version number is published. The National Logbook Register launched in 2022; Register v1.0 was announced 27 March 2023. **[verified: primary]**
- **Is it keyed on UPRN?** RLBA's own pages do not say so; the Register is "a verified record of logbooks for UK addresses". **[verified: primary]**
  - An independent site says logbook data "is stored against the property's Unique Property Reference Number (UPRN)". https://www.logbook.co.uk/uk-property-logbook-providers-rlba-landscape/ **[secondary]**
- **How to join and cost** **[verified: primary]** https://www.rlba.org.uk/membership:
  - Membership is annual and renews each January. Contact chair@rlba.org.uk.
  - "From 2026 the Logbook Membership fee will be set at **£500 per annum**"; Associate membership is **£250**; Stakeholder membership is **free**.
  - Listing logbooks requires compliance with "the RLBA technical specification".
- **Related bodies** **[verified: primary]**:
  - **OPDA:**
    - Its Property Data Trust Framework (PDTF) API is **UPRN-keyed**: "Returning the JSON representation of the current state of the property data for a given UPRN" (https://openpropdata.org.uk/for-developers/).
    - Membership is £3k, £6k or £10k a year by turnover (https://openpropdata.org.uk/become-a-member/).
    - OPDA's own view (not government policy) is that mandation is expected by 2029 and a smart data scheme by 2030.
  - **RLBA:** "Our member logbooks are on a path to being PDTF compliant" (2023).
  - **BASPI:** developed by the HBSC with the Conveyancing Association, with Part A (material information) and Part B (legal). No version is shown on the HBSC page; "v5" is **[secondary]**. https://www.homebuyingsellingcouncil.co.uk/BASPI-Buyers-and-Sellers-Property-Information

## 9. Smart data for property

- **The call for evidence is open.** DBT's *Smart Data: multi-sector call for evidence* (CP 1608) covers "agri-food, property, retail, trade and transport". "Published 8 July 2026"; it "closes at 11:59pm on **1 October 2026**", so it is **open as of today**. https://www.gov.uk/government/calls-for-evidence/smart-data-multi-sector-call-for-evidence **[verified: primary]**
- **Its property section** estimates "£28.7 billion in net social value between 2028 and 2043 and £4.2 billion in GDP every year". It names Moverly as a Smart Data Challenge Prize winner. **[verified: primary]**
- **Flag:** it is unconfirmed whether this DBT call meets the roadmap's promised property call for evidence or whether a separate MHCLG one will follow. A consultation on the property scheme is due in 2027.
- **Legal basis:** Data (Use and Access) Act 2025 Part 1, ss.1–26. **[verified: primary]**
  - s.2 (customer data) and s.4 (business data) are the regulation-making powers.
  - s.7 covers interface bodies; ss.8–10 enforcement; ss.11–13 fees and levy.
  - Part 1 has been **in force from 20 August 2025** under SI 2025/904 reg 2(a). https://www.legislation.gov.uk/uksi/2025/904/regulation/2/made
  - No property-sector smart data regulations have been made. **[inferred]**

## 10. Material information in property listings

**⚠ The NTSELAT guidance was withdrawn in May 2025.**
- **Part A** (price, "the council tax band (or property rates information in Northern Ireland)", tenure) was published 12 July 2022. https://www.nationaltradingstandards.uk/news/national-trading-standards-publishes-guidance-on-part-a-material-information-for-property-listings **[verified: primary]**
- **Parts B and C** were published 30 November 2023: Part B "such as the type of property, the building materials used, the number of rooms and information about utilities and parking"; Part C covers matters "such as flood risk or restrictive covenants". https://www.nationaltradingstandards.uk/news/full-material-information-guidance-published/ **[verified: primary]**
- **Withdrawn** "Effective 8th May 2025", because the Consumer Protection from Unfair Trading Regulations were "superseded and replaced by the new Digital Markets, Competition and Consumers Act 2024". https://todaysconveyancer.co.uk/ntselat-material-information-guidance-withdrawn-but-duty-remains/ ; Propertymark agrees. **[secondary]**
- **The NTS page now** says only that MHCLG "announced its intention to introduce homebuying sales packs … in June 2026". https://www.nationaltradingstandards.uk/work-areas/estate-agency-team/material-information/ **[verified: primary]**

**Current requirement: the DMCCA 2024 statute, pending MHCLG guidance** **[verified: primary]**
- **s.225:** unfair commercial practices are prohibited, including where a practice "omits material information from an invitation to purchase (see section 230)". It is in force from 6 April 2025 (SI 2025/272). https://www.legislation.gov.uk/ukpga/2024/13/section/225
- **s.227(2):** "'material information' means information that the average consumer needs to take an informed transactional decision". https://www.legislation.gov.uk/ukpga/2024/13/section/227
- **Roadmap commitment:** "non-statutory guidance … explain existing responsibilities under the Digital Markets, Competition and Consumers Act 2024 with a view to ensuring that no further legislation on material information is required". It also promises a standardised material information form, and says "title information should only be obtained from HMLR". **Not yet published** as far as I found.
- **Council tax band.** It was an explicit Part A item under the withdrawn guidance, and it is in the roadmap's Annex B sales-pack list. Under the DMCCA today it is required only in so far as it is "material information" under s.227 and s.230. **[inferred]**

**Enforcement** **[verified: primary]** https://www.nationaltradingstandards.uk/work-areas/estate-agency-team/
- "the estate agency lead enforcement authority is operated from Powys County Council and the letting agency … is hosted by Bristol City Council". It is funded by MHCLG.

---

# PART C — Exit comparables (UK property data and proptech M&A, 2021 to today)

## 11. Deals

| # | Buyer | Target | Date | Price | Multiple | Source / tag |
|---|---|---|---|---|---|---|
| 1 | ATI Global (InfoTrack parent) | **Groundsure** (from Ascential) | 20 Jan 2021 | "**£170m** comprises an initial cash consideration of £140m … plus a £30m … vendor loan note" | FY2019 revenue £20.0m; adjusted EBITDA before central costs £12.4m (£10.6m after). **≈8.5x revenue; ≈13.7–16.0x EBITDA** [inferred]. Trade press "18x" not reconciled | Ascential RNS 2941M https://www.investegate.co.uk/announcement/rns/ascential--ascl/sale-of-groundsure-for-170m/6142533 **[verified: primary]** |
| 2 | ATI Global / InfoTrack | **Search Acumen** | Feb–Mar 2021 | Undisclosed | — | **[secondary, search extract only]** |
| 3 | Dye & Durham | **Terrafirma** | 12 May 2021 | "approximately $20 million (£12 million)" | — | https://dyedurham.com/terrafirma-acquired-by-dye-durham/ **[verified: primary]** |
| 4 | Dye & Durham | **TM Group** | 8 Jul 2021 | "approximately $156 million (£91.5 million)" | ≈11.9x adjusted EBITDA if EBITDA ≈£7.7m **[secondary EBITDA; inferred]** | https://dyedurham.com/dye-durham-acquires-tm-group-uk-limited/ **[verified: primary]** |
| 4b | AURELIUS | **TM Group** (divested after the CMA ruling, Aug 2022) | Agreed 10 Jul 2023; completed 10 Aug 2023 | "approximately **£50 million** in cash at closing, with up to £41 million in potential additional earn-out" | ≈6.5x (stale) EBITDA on cash **[inferred]** | https://dyedurham.com/dye-durham-completes-sale-of-tm-group-for-up-to-91-million/ **[verified: primary]** |
| 5 | Inspirit Capital | **Landmark Solutions** (division of Landmark) | Sep 2021 | Undisclosed | — | https://www.privateequitywire.co.uk/inspirit-capital-acquires-geospatial-data-services-specialist-landmark-solutions/ **[secondary]** |
| 6 | PEXA | **Optima Legal** (from Capita) | Announced 8 Sep 2022; completed Dec 2022 | Undisclosed | ~22% of the remortgage market | https://www.pexa.com.au/company-news/pexa-continues-uk-expansion-with-optima-legal-acquisition/ **[verified: primary]** |
| 7 | PriceHubble | **Dataloft** | 20 Mar 2023 | Undisclosed | — | https://www.pricehubble.com/uk/pricehubble-news/pricehubble-acquires-dataloft-to-accelerate-its-growth-in-the-uk **[verified: primary]** |
| 8 | **CoStar** | **OnTheMarket plc** | Announced 19 Oct 2023; effective 12 Dec 2023 | "110 pence per share … approximately **£99 million**". 10-K: total consideration £96.0m ($120.4m) | FY Jan-2023 revenue £34.4m, so **≈2.8–2.9x revenue on equity value** **[secondary revenue; inferred]** | Nasdaq copy of CoStar release; CoStar FY2023 10-K https://www.sec.gov/Archives/edgar/data/1057352/000105735224000013/csgp-20231231.htm **[verified: primary]**; (blocked: costargroup.com, 403) |
| 9 | PEXA | **Smoove plc** | Announced 5 Oct 2023; effective 19 Dec 2023 | "54 pence in cash … values Smoove at **£30.8 million**" (£20.8m net of cash) | FY23 revenue £20.6m and an EBITDA loss, so **≈1.0–1.5x revenue** **[inferred]** | https://www.pexa-group.com/content-hub/news/pexa-group-acquisition-of-smoove-plc/ **[verified: primary]** |
| 10 | Accel-KKR | **Reapit + PayProp** combination | 5 Dec 2023 | Undisclosed | — | https://www.reapit.com/press-releases/reapit-and-payprop-join-forces-backed-by-accel-kkr-investment **[verified: primary]** |
| 11 | LandTech | **Built-ID** | Dec 2023 / Jan 2024 | Undisclosed | — | **[secondary, search extract only]** |
| 12 | Rightmove | **HomeViews** | 1 Feb 2024 | "cash consideration of **£8 million**" | — | https://www.rightmove.co.uk/press-centre/rightmove-acquires-reviews-platform-homeviews/ **[verified: primary]** |
| 13 | Lloyds (lead), Nationwide, NatWest, Rightmove | **Coadjute** (minority) | 2 Apr 2024 | "£3 million as part of a £10 million funding round"; £23m cumulative | — | https://www.coadjute.com/resources/press-release-strategic-investment **[verified: primary]** |
| 14 | iamproperty | **Information Works** | Feb 2024 | Undisclosed | — | **[secondary, search extract only]** |
| 15 | TM Group (AURELIUS) | **Lawtech Software Group** | Mar 2024 | Undisclosed | — | **[secondary, search extract only]** |
| 16 | REA Group (approach, lapsed) | **Rightmove plc** | 2–30 Sep 2024: four proposals (705p → 749p → 770p → **781p**), all rejected | 781p ≈ "**£6.2 billion**" | "an enterprise value multiple of approximately **22.7x** Rightmove's EBITDA for the twelve months ended 30 June 2024 of £272 million" (REA's own figure) | REA announcement https://www.sec.gov/Archives/edgar/data/1564708/000156470824000504/a092724991-reaannouncement.htm **[verified: primary]** |
| 17 | TM Group | **Veya** | Mar 2025 | Undisclosed | — | PitchBook **[secondary, unconfirmed]** |
| 18 | iamproperty | **The ValPal Network** (AVM / valuation leads) | Jan 2026 | Undisclosed | — | https://iamproperty.com/news/iamproperty-acquires-the-valpal-network/ **[verified: primary]** |
| 19 | Hg (minority) | **Street Group** | 22 Jul 2026 | "valuing the company at **more than £200m**"; founders remain majority owners | — | https://hgcapital.com/insights/street-group-secures-a-strategic-growth-investment-from-hg **[verified: primary]** |
| 20 | Providence Equity | **Hometrack** (from ZPG/Silver Lake) | Announced 14 Aug 2026; "subject to customary regulatory approvals" | **Undisclosed.** Reported ≈£600m (Real Deals, paywalled) | Asymmetrix: "£600m enterprise value implies a roughly **10x revenue** multiple". Older published revenue (£21–22m) would imply ≈27x, so **unconfirmed** | https://www.hometrack.com/blog/providence-acquisition/ **[verified: primary]**; https://asymmetrixintelligence.substack.com/p/hometrack-sells-for-a-reported-600m **[secondary]**; (blocked: provequity.com, 403) |
| — | *Context (US):* CoStar | Matterport | Announced 22 Apr 2024 | "$1.6 billion of enterprise value" | — | CoStar 8-K **[verified: primary]** |

**⚠ Names from the brief:**
- **Landmark Information Group was not sold to Astorg.**
  - Companies House today: Landmark (02892803) → DMGI Land & Property Europe Ltd → DMG Information Ltd, i.e. still DMGT. https://find-and-update.company-information.service.gov.uk/company/02892803/persons-with-significant-control **[verified: primary]**
  - Its only 2021+ deal found is selling Landmark Solutions (row 5).
- **TwentyCi / TwentyEA:** sale rumours in March 2023 ("I can confirm that these are rumours"); no completed sale. https://thenegotiator.co.uk/news/property-data-firm-twentyci-responds-to-industry-rumours-of-a-sale/ **[secondary]**
- **Zoopla / Houseful:**
  - Reportedly for sale at about £500m (April 2025). https://propertyindustryeye.com/breaking-news-zoopla-up-for-sale-with-500m-asking-price/ **[secondary]**
  - Silver Lake hired banks for a strategic review (September 2025). **[secondary]**
  - The Hometrack sale (row 20) is the first disposal. No sale of Zoopla or Alto has been announced.
- **PropertyData:** ⚠ the 2021 "Hutly acquires PropertyData" deal is the Australian REIV platform, not propertydata.co.uk (Liberty Tech Ltd). No UK deal was found. **[secondary]**
- **LandTech / LandInsight:** ⚠ the September 2025 "Land Insight" deal involves an Australian firm. LandTech raised a €49.4m Series A in 2021 **[secondary]**; no sale.
- **No acquisition found** for **Sprift, Nimbus Maps, Searchland or Moverly**. Moverly has had seed rounds only, about $1.03m in September 2024 **[secondary]**.

## 12. Active acquirers and published multiples

**Trade buyers active in 2021–26** (from the table):
- InfoTrack/ATI Global
- CoStar
- Rightmove
- iamproperty
- TM Group (AURELIUS)
- Reapit (Accel-KKR)
- PriceHubble
- LandTech

**Trade buyers less active now** **[inferred]**:
- **Dye & Durham:** forced by the CMA to sell TM Group in 2023.
- **PEXA:** wrote down its UK assets in FY2025 and put its Digital division under review **[secondary]**.

**Private equity:** Providence (Hometrack), Hg (Street Group), Accel-KKR (Reapit), AURELIUS (TM Group), Inspirit (Landmark Solutions). Silver Lake is now a seller.
- No 2021–26 UK property-data deals were found for Astorg, Bridgepoint, Inflexion, Horizon, LDC or Livingbridge, though I did not search each individually.

**Advisers on the Hometrack sale:** Arma Partners and J.P. Morgan for the sellers; Deutsche Bank and Rothschild for Providence. **[secondary]**

**Published sector multiples:**
- **Fortlane Partners, *PropTech – September 2025 – Market Overview and M&A Activity*** (data to 16 September 2025) **[secondary, PDF opened]**: https://www.fortlane.com/_Resources/Persistent/e/a/f/6/eaf60a4bf02198bceea6218d975036d851a6101b/2025-09_Fortlane_PropTech_M&A%20Report.pdf
  - Precedent deals: "median EV/ Sales multiple of **8.5x** and a median EV/ EBITDA multiple of **22.7x**".
  - Real estate marketplaces: "median EV/ Sales multiple of 10.7x".
- **Asymmetrix:** Hometrack at "roughly 10x revenue" (27 August 2026). **[secondary]**
- **Trading multiples today** (StockAnalysis.com, "Last updated: Sep 26, 2026"; not checked against an exchange feed) **[secondary]**:
  - **Rightmove:** EV/EBITDA **10.9x**, EV/Sales 7.4x, share price −38% over 52 weeks. That is less than half REA's 22.7x bid multiple **[inferred]**.
  - **CoStar:** EV/EBITDA 28.6x, EV/Sales 3.2x, share price −67% over 52 weeks.
- **Deal-implied multiples** (from the table, **[inferred]**):
  - Groundsure: 8.5x revenue.
  - OnTheMarket: 2.9x revenue.
  - Smoove: 1.0–1.5x revenue.
  - TM Group: about 12x EBITDA.
  - Rightmove/REA: 22.7x EBITDA.
- No dated UK figures from Houlihan Lokey, Clearwater, Arma or the UK PropTech Association were found.

---

# Summaries

**Part A — Why addresses are still a mess.**
- **The council tax list rests on a rushed 1991–93 exercise.**
  - About 21 million dwellings were banded against a 1 April 1991 value.
  - The VOA's own manual says it was done mostly "at the desk", and "Very few properties were externally inspected".
  - Private contractors did roughly half the work, for £19m, after ministers had budgeted £250m.
  - 914,196 challenges followed in the first eight months.
  - About 1.31m bands have been reduced on challenge since 1993.
- **The VOA admits its property records were poor.** In April 1993, 35% of properties had an unknown type and 37% an unknown build period. It still cannot review improvements until a sale, and it asks owners to "estimate" their build year on its own form.
- **The UPRN has existed since 1999 but was paid-for until 2020.**
  - It came out of the council-built NLPG under BS 7666.
  - GeoPlace (LGA and OS, 2010–11) and AddressBase (2011) followed.
  - Identifiers only became free (OGL) on 1 July 2020, and only as numbers and coordinates.
- **Address text is still paid for.** It sits in AddressBase and Royal Mail's PAF. The PAF stayed with Royal Mail at privatisation and is now owned via EP Group. Government pays £30.8m for 2023–28 so the public sector can use it free, and commercial prices rise on 1 October 2026.
- **The flagship address product is being replaced.** AddressBase and AddressBase Plus reach end of life in autumn 2027. Their successor, OS GB Address, is updated daily, tracks each address through its lifecycle, and cross-references UPRNs to VOA council tax UARNs, but not to bands. It remains a paid licence.
- **UPRN coverage in public data is patchy.**
  - Energy performance certificates have UPRNs since November 2021.
  - Land Registry price-paid data gained a UPRN lookup only on 28 August 2026, for new records.
  - The VOA's own lists are keyed on its UARN, and it refuses to publish a UARN–UPRN link.
- **No official estimate of what poor addressing costs the UK exists.**

**Part B — Logbooks and property data rules.**
- **The June 2026 roadmap.** MHCLG's roadmap (19 June 2026) commits to mandatory sales packs, binding contracts, and digital logbooks with a minimum standard data set. All of these are "when parliamentary time allows", with no bill named. Guidance, a Code of Practice and a smart data call for evidence are promised for 2026, and data-standard accreditation and a smart data consultation for 2027–28.
- **UPRN is no longer mentioned.** The October 2025 consultation spoke of a UPRN-linked core data set; the final roadmap drops UPRN.
- **The Land Registry trial.** A 12-month HMLR/RLBA proof of concept began in June 2026: four unnamed logbook providers and up to 2,500 title data requests.
- **The RLBA.** It is at rlba.org.uk and charges £500 a year for logbook members. Its Core Logbook standard dates from 2020; being UPRN-keyed is claimed only by a third party. OPDA's trust framework API is UPRN-keyed.
- **Smart data.** DBT's multi-sector smart data call for evidence, including property, closes 1 October 2026. The legal powers (Data (Use and Access) Act 2025 Part 1) have been in force since August 2025.
- **Material information.** The NTSELAT guidance, which listed council tax band as a Part A item, was withdrawn in May 2025. Listings now rely on DMCCA 2024 ss.225, 227 and 230 until MHCLG's promised guidance appears.

**Part C — Exit comparables.**
- **Deals with public data:**
  - Groundsure: £170m, about 8.5x revenue (2021).
  - TM Group: £91.5m (2021), then resold after the CMA ruling for £50m plus up to £41m earn-out (2023).
  - OnTheMarket: £99m to CoStar, about 2.9x revenue (2023).
  - Smoove: £30.8m to PEXA, about 1.5x revenue (2023).
  - Rightmove: REA's lapsed £6.2bn approach at 22.7x EBITDA (2024).
  - Street Group: Hg minority investment at a valuation above £200m (2026).
  - Hometrack: pending sale to Providence at a reported but undisclosed £600m, estimated at about 10x revenue (2026).
- **Several comparables in the brief are not real deals:** Landmark, PropertyData, LandInsight and others.
- **Active buyers:** InfoTrack, CoStar, Rightmove, iamproperty, TM Group, Reapit, plus Providence and Hg.
- **Sector multiples:** the one dated published source (Fortlane, September 2025) gives medians of 8.5x revenue and 22.7x EBITDA. Listed comparables have de-rated sharply: Rightmove is at about 11x EBITDA today.

# Ten facts most useful to a pitch or funding document (public, citable)

1. **"Very few properties were externally inspected."** Most of about 21m homes were banded "at the desk" in 1991–92 (VOA Council Tax Manual, Section 1, para 2.2; VO Annual Report 1993–94). **[verified: primary]**
2. **In April 1993 the VOA did not know the property type of 35% of homes or the build period of 37%** (Council Tax: stock of properties 2026, background information, section 3.4). **[verified: primary]**
3. **The VOA's own band challenge form asks owners: "Year property built: If unknown please estimate year here"** (Form VO 7455 (10/25)). **[verified: primary]**
4. **About 1.31 million bands have been reduced on challenge since 1993**, about 46% of resolved challenges (VOA challenges and changes time series to 2023–24; my sum). **[inferred from primary]**
5. **Since 1 July 2020 government systems "must use the UPRN and USRN identifiers"** for property and street data (GOV.UK open standard). The free OS Open UPRN still contains **no address text**. **[verified: primary]**
6. **Government pays £30.8m (2023–28) to Royal Mail** so the public sector can use the PAF free, on top of the **£962.9m** PSGA with Ordnance Survey (2020–30) (Contracts Finder). **[verified: primary]**
7. **Land Registry price-paid data has no UPRN.** A UPRN lookup was first published on **28 August 2026**, covering new records only (gov.uk). **[verified: primary]**
8. **Government has committed to legislate** to make digital property logbooks and sales packs "a requirement for all property transactions when parliamentary time allows". 82% of consultation responses supported logbooks (MHCLG roadmap, 19 June 2026). **[verified: primary]**
9. **The DBT smart data call for evidence puts the property scheme's value at £28.7bn net social value (2028–43)** and £4.2bn GDP a year. It closes 1 October 2026 (CP 1608). **[verified: primary]**
10. **Recent exits:**
    - Groundsure sold for **£170m (≈8.5x revenue)** in 2021 (Ascential RNS).
    - CoStar bought OnTheMarket for **£99m** in 2023.
    - REA valued Rightmove at **22.7x EBITDA** in 2024.
    - The primary sources for these are listed in section 11.

# Claims I could not verify

**Part A**
- **1991 banding:**
  - Staff and contractor numbers; the contractor share of properties; the final total cost. The NAO report HC 1993-94 320 is the key missing source (blocked: webarchive.nationalarchives.gov.uk, 405).
  - "10 minutes per property", "drive-by" and "rough and ready" are not found in any official source.
  - Pickles's 1% and 6.3% contractor accuracy figures are uncorroborated.
- **Other sources not reached:** Commons Library briefings (blocked, 403); IFS revaluation reports (blocked, 403); Lyons interim papers (blocked, 403); 1994 PAC report (not found).
- **VOA systems:**
  - Whether the band-checker result page shows a UPRN (blocked, 403).
  - Whether the VOA's 2025 system stores UPRNs.
  - The UKAuthority "legacy systems" quote (blocked; search extract only).
- **Standards and licensing:**
  - Which BS 7666 parts existed in 1994.
  - The OSMA start date.
  - The PSMA "10-year" term.
  - The PAF Public Sector Licence 2020–23 value of £15.75m (blocked: bidstats.uk).
  - The current GeoPlace profit split.
- **PAF regulation:** Ofcom's 2013 PAF statement and any later review (blocked: ofcom.org.uk, 403). PASC report HC 564 read only as quoted by ODUG (blocked: publications.parliament.uk, 403).
- **UPRN datasets:**
  - Start dates for UPRN in schools data (GIAS), CQC, NHS ODS and planning.data.gov.uk.
  - Environment Agency datasets (blocked).
  - The licence conflict on the HMLR title number–UPRN lookup.

**Part B**
- The HLWS134 statement text (blocked, 403).
- Whether MHCLG's Code of Practice or listing guidance has been published since June (not found; estateagenttoday.co.uk blocked).
- The four logbook providers in the HMLR trial.
- RLBA standard version and UPRN keying (third-party claim only); full current member list.
- BASPI version number and PDTF schema version (github.com blocked, 403).
- Whether DBT's call for evidence is the one the roadmap promised.

**Part C**
- Hometrack's price, revenue and completion (terms undisclosed; provequity.com blocked).
- Undisclosed prices: Search Acumen, Optima Legal, Built-ID, Dataloft, Information Works, ValPal, Veya.
- TM Group's £7.7m EBITDA and whether the AURELIUS earn-out was paid.
- OnTheMarket's net cash.
- The Groundsure "18x EBITDA" trade-press figure.
- Zoopla/Alto sale outcome.
- Any Experian, Verisk or LexisNexis UK property-data deal.
- CoStar's own press pages (blocked, 403).
- Current trading multiples: third-party site, not an exchange feed.
