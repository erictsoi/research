# Perplexity prompt pack — completing the premium & finance gaps

**Date:** 27 September 2026  
**Purpose:** fill the fields this cloud session could not read (Cloudflare/bot-gated council pages, unconfirmed triggers, legal-precedent gaps) so they fold back into `data/premium_pressure_2025.csv` and the Brief 3/4 reports.

**How to use:** run one prompt per entity (Perplexity handles a single focused entity per query far better than a long list). Each prompt forces a fixed answer format **and** a one-line CSV row so results paste straight back. Councils are tagged with their **ONS code** to disambiguate same-named authorities.

**Fold-back:** collect the emitted CSV rows into a text file and hand them back to this session (or the local lane). I will reconcile each against the existing table, overwrite `trigger`/rates where the source URL confirms it, and leave `unclear` rows flagged for manual follow-up. Trust only rows whose `Source_URL` is the council's **own** domain.


---

## Section 1 — the 96 unknown-trigger councils (1-year vs 2-year)

These adopt the empty-homes premium but told MHCLG they can't identify 1–2yr dwellings, so the trigger year is unknown from data. One prompt each.

**Reusable template** (replace `[COUNCIL]`):

```
For [COUNCIL] council in England, what is its 2025/26 long-term empty homes council tax premium?
- Does the premium start when a home has been empty 1 year or 2 years?
- What are the premium rates at 1, 5 and 10 years empty (as % on top of standard council tax, e.g. 100% / 200% / 300%)?
- Use ONLY the council's own council-tax / empty-homes page. Give the exact https URL.
Answer in this exact format:
Council: [COUNCIL]
Trigger: [1 year / 2 years / unclear]
Rate_1yr: [e.g. 100% / N/A]
Rate_5yr: [e.g. 200% / N/A]
Rate_10yr: [e.g. 300% / N/A]
Source_URL: [full https URL to the council's own page]
Notes: [caveats, e.g. exceptions, date effective]
Also output one CSV row, no header, exactly:
[COUNCIL],[ONS],[Trigger],[Rate_1yr],[Rate_5yr],[Rate_10yr],[Source_URL],[Notes]
```

**The 96 councils** (ONS code · name · region):

1. `E07000067` — **Braintree** (E)
2. `E07000144` — **Broadland** (E)
3. `E06000056` — **Central Bedfordshire** (E)
4. `E07000096` — **Dacorum** (E)
5. `E07000242` — **East Hertfordshire** (E)
6. `E07000145` — **Great Yarmouth** (E)
7. `E07000073` — **Harlow** (E)
8. `E07000202` — **Ipswich** (E)
9. `E07000146` — **King's Lynn and West Norfolk** (E)
10. `E07000099` — **North Hertfordshire** (E)
11. `E06000031` — **Peterborough** (E)
12. `E07000012` — **South Cambridgeshire** (E)
13. `E07000149` — **South Norfolk** (E)
14. `E07000243` — **Stevenage** (E)
15. `E07000076` — **Tendring** (E)
16. `E07000077` — **Uttlesford** (E)
17. `E07000103` — **Watford** (E)
18. `E07000172` — **Broxtowe** (EM)
19. `E07000034` — **Chesterfield** (EM)
20. `E07000035` — **Derbyshire Dales** (EM)
21. `E07000036` — **Erewash** (EM)
22. `E07000173` — **Gedling** (EM)
23. `E07000037` — **High Peak** (EM)
24. `E07000132` — **Hinckley and Bosworth** (EM)
25. `E06000016` — **Leicester** (EM)
26. `E07000138` — **Lincoln** (EM)
27. `E07000175` — **Newark and Sherwood** (EM)
28. `E07000038` — **North East Derbyshire** (EM)
29. `E07000139` — **North Kesteven** (EM)
30. `E06000061` — **North Northamptonshire** (EM)
31. `E07000135` — **Oadby and Wigston** (EM)
32. `E06000017` — **Rutland** (EM)
33. `E07000039` — **South Derbyshire** (EM)
34. `E07000141` — **South Kesteven** (EM)
35. `E09000002` — **Barking and Dagenham** (L)
36. `E09000006` — **Bromley** (L)
37. `E09000001` — **City of London** (L)
38. `E09000009` — **Ealing** (L)
39. `E09000014` — **Haringey** (L)
40. `E09000016` — **Havering** (L)
41. `E09000019` — **Islington** (L)
42. `E09000020` — **Kensington and Chelsea** (L)
43. `E09000024` — **Merton** (L)
44. `E09000027` — **Richmond upon Thames** (L)
45. `E09000032` — **Wandsworth** (L)
46. `E06000047` — **Durham** (NE)
47. `E08000037` — **Gateshead** (NE)
48. `E06000001` — **Hartlepool** (NE)
49. `E08000021` — **Newcastle upon Tyne** (NE)
50. `E08000022` — **North Tyneside** (NE)
51. `E08000023` — **South Tyneside** (NE)
52. `E06000008` — **Blackburn with Darwen** (NW)
53. `E08000002` — **Bury** (NW)
54. `E06000049` — **Cheshire East** (NW)
55. `E08000004` — **Oldham** (NW)
56. `E08000009` — **Trafford** (NW)
57. `E07000128` — **Wyre** (NW)
58. `E07000084` — **Basingstoke and Deane** (SE)
59. `E07000085` — **East Hampshire** (SE)
60. `E07000208` — **Epsom and Ewell** (SE)
61. `E07000209` — **Guildford** (SE)
62. `E07000062` — **Hastings** (SE)
63. `E07000228` — **Mid Sussex** (SE)
64. `E07000178` — **Oxford** (SE)
65. `E07000064` — **Rother** (SE)
66. `E07000213` — **Spelthorne** (SE)
67. `E07000214` — **Surrey Heath** (SE)
68. `E07000215` — **Tandridge** (SE)
69. `E07000093` — **Test Valley** (SE)
70. `E07000115` — **Tonbridge and Malling** (SE)
71. `E06000037` — **West Berkshire** (SE)
72. `E07000181` — **West Oxfordshire** (SE)
73. `E06000040` — **Windsor and Maidenhead** (SE)
74. `E07000079` — **Cotswold** (SW)
75. `E07000080` — **Forest of Dean** (SW)
76. `E07000043` — **North Devon** (SW)
77. `E06000025` — **South Gloucestershire** (SW)
78. `E07000083` — **Tewkesbury** (SW)
79. `E06000027` — **Torbay** (SW)
80. `E07000234` — **Bromsgrove** (WM)
81. `E07000192` — **Cannock Chase** (WM)
82. `E07000235` — **Malvern Hills** (WM)
83. `E07000236` — **Redditch** (WM)
84. `E07000220` — **Rugby** (WM)
85. `E06000051` — **Shropshire** (WM)
86. `E07000196` — **South Staffordshire** (WM)
87. `E07000197` — **Stafford** (WM)
88. `E07000198` — **Staffordshire Moorlands** (WM)
89. `E07000221` — **Stratford-on-Avon** (WM)
90. `E06000020` — **Telford and Wrekin** (WM)
91. `E07000222` — **Warwick** (WM)
92. `E07000237` — **Worcester** (WM)
93. `E07000238` — **Wychavon** (WM)
94. `E08000033` — **Calderdale** (YH)
95. `E06000010` — **Kingston upon Hull** (YH)
96. `E08000018` — **Rotherham** (YH)

> Bulk tip: the machine-readable list is in `requests/2026-09-27_unknown-trigger-councils.csv` (ons, la, region). Loop the template over the `la` column.


---

## Section 2 — finance / premium term gaps (specific flagged councils)

For each, confirm the empty-homes AND second-home premium terms, plus any buyer-usable loan/grant scheme.

```
For [COUNCIL] council, confirm for 2025/26:
1. Long-term empty homes premium — trigger (1 or 2 years) and rates at 1/5/10 years.
2. Second-home premium — adopted? from what date? what rate?
3. Any empty-homes loan or grant a BUYER of an empty home could use (amount, term, interest, security, strings such as let-to-council/nomination/clawback, and whether currently open).
Use the council's own pages and any linked scheme PDF. Give exact https URLs.
Answer:
Council: [COUNCIL]
LTE_trigger: [1 year / 2 years / unclear]
LTE_rates_1_5_10: [e.g. 100/200/300 %]
Second_home_premium: [Yes+rate+date / No / unclear]
Buyer_scheme: [describe or 'none found']
Scheme_strings: [let-back years / nomination / clawback / none]
Scheme_open: [open / closed / suspended / unclear]
Source_URLs: [one or more https URLs]
```

Run for: **Hart**, **Surrey Heath**, **North Lincolnshire**, **Spelthorne**, **Bracknell Forest**, **Woking**, **Guildford**, **Barnsley** (find the empty-home grant terms PDF), **Newcastle upon Tyne** (find 'Grant Scheme 1: Empty Properties').


---

## Section 3 — the other dead-ends

### 3a. Bona vacantia / Treasury Solicitor auction lots

```
Do UK residential property auctions ever list lots sold "by order of the Treasury Solicitor" or the Government Legal Department / Bona Vacantia Division?
- Which auction houses handle Crown / bona vacantia / dissolved-company property?
- Link at least one real past catalogue lot (with URL) showing this wording.
Give auction house, lot description, date, and URL. If none can be found, say so plainly.
```

### 3b. VAT tribunal case law on empty-period evidence (5% / zero rate)

```
Find UK First-tier Tribunal (Tax) or Upper Tribunal decisions on the 5% reduced or zero VAT rate for renovating dwellings empty 2+ or 10+ years — specifically disputes over what EVIDENCE proves the empty period (e.g. Empty Property Officer letters, council tax records).
Give case name, neutral citation, year, a one-line summary of the evidence issue, and a URL (BAILII / gov.uk / tribunal decisions). List each case separately.
```

### 3c. ICO enforcement on reusing published-notice data for marketing

```
Any ICO (UK Information Commissioner) enforcement actions, decision notices, or reprimands about organisations reusing PUBLICLY PUBLISHED data (e.g. The Gazette statutory notices, insolvency/probate/deceased-estate notices, land/company registers) for DIRECT MARKETING under UK GDPR or PECR?
Give the organisation, date, outcome, a one-line summary, and a URL to the ICO decision/press release. If none specific to published-notice reuse exist, give the nearest analogous cases.
```

### 3d. LAHF per-council allocations

```
Provide a per-council breakdown of Local Authority Housing Fund (LAHF) allocations in England, all rounds (1-4).
- For each council: total allocated and which round(s).
- Cite official gov.uk / MHCLG sources. If no single table exists, give the best official round pages plus any reputable aggregation, with URLs.
```

### 3e. FixMyStreet report-data reuse licence

```
Under what licence can the report data from FixMyStreet (mySociety) be reused, including for research or a commercial product? Is the report data (not the AGPL software) covered by OGL, Creative Commons, or a bespoke licence? Quote mySociety's own terms/FAQ with the URL.
```

### 3f. Policy in Practice 'Missing Out 2026' (F12 re-check)

```
Has Policy in Practice published its 'Missing Out' report for 2026 (unclaimed benefits / Council Tax Support in Great Britain)? If so, give the headline unclaimed totals (total and Council Tax Support specifically), publication date, and the URL.
```


---

## Section 4 — what I do with the results

Hand back the collected CSV rows (Section 1) and the Section 2–3 answers. I will: (1) update `trigger`, rates and second-home fields in `data/premium_pressure_2025.csv` from council-own-domain sources, re-run the bite score, and note which rows moved from `unknown`; (2) fold the finance terms into the Brief 4 report and drop the `[secondary]`/`(verify)` flags where a primary URL now confirms them; (3) add any real VAT/ICO cases to the Brief 3 legal items and the auction finding to the bona-vacantia note. Rows without a council-own-domain source stay flagged, not merged.
