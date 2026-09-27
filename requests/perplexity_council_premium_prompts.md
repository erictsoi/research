# Perplexity prompt pack v2 — completing the premium & finance gaps

**Date:** 27 September 2026  
**Purpose:** fill the fields this session could not read (bot-gated council pages, unconfirmed triggers, legal-precedent gaps) so they fold back into `data/premium_pressure_2025.csv` and the Brief 3/4 reports.

**How to use:** one prompt per entity (Perplexity handles a single focused entity far better than a list). Each forces a fixed answer format **and** a CSV row. Councils carry their **ONS code** to disambiguate same-named authorities and to key the merge.

### Validation rules (apply to every answer)

- Use the council's **own website or an official council PDF** as primary source. Do **not** infer the trigger from national legislation alone.
- Distinguish the **premium trigger** (how long empty before a premium starts) from the **date a rate changed**.
- **A missing figure is NOT evidence that no premium exists.** Use `N/A` only where the official source clearly establishes the rate is not applicable; otherwise write `unclear` and keep the source URL for manual review.
- Preserve the **exact ONS code** given for each council in the CSV row.


---

## Section 1 — 96 unknown-trigger councils (1-year vs 2-year), by priority

Sorted by `bite_score` (premium-pressure value of resolving it). Reusable template — replace `[COUNCIL]` and `[ONS]`:

```
For [COUNCIL], confirm the 2025/26 long-term empty homes council tax premium.
Answer in this exact format:
ONS: [ONS]
Council: [official council name]
Trigger: [1 year / 2 years / other / unclear]
Rate_1yr: [percentage or N/A]
Rate_5yr: [percentage or N/A]
Rate_10yr: [percentage or N/A]
Type: [long-term empty homes / second home / both / unclear]
Effective_year: [year]
Source_URL: [council-owned URL]
Source_title: [page or PDF title]
Evidence_quote: "[short exact quotation]"
Notes: [transitional rules, exemptions, or uncertainty]
Use the council's own website or an official council PDF. Do not infer the trigger from national legislation alone. Distinguish the premium trigger from the date a rate changed. If evidence is incomplete, write unclear rather than guessing.
Finally, output one CSV row with no header, in this exact order:
ons,la,trigger,rate_1yr,rate_5yr,rate_10yr,type,effective_year,source_url,source_title,evidence_quote,notes
Quote fields containing commas or quotes per standard CSV rules. Preserve this ONS code exactly: [ONS]
```

**Priority batch (top 17 by bite score):**

| # | Council | ONS | Region | Band D | Bite |
|---:|---|---|---|---:|---:|
| 1 | Rutland | `E06000017` | EM | £2671 | 82 |
| 2 | Oxford | `E07000178` | SE | £2557 | 80 |
| 3 | Rother | `E07000064` | SE | £2561 | 80 |
| 4 | Durham | `E06000047` | NE | £2551 | 79 |
| 5 | Hastings | `E07000062` | SE | £2554 | 79 |
| 6 | Gedling | `E07000173` | EM | £2507 | 77 |
| 7 | North Devon | `E07000043` | SW | £2515 | 77 |
| 8 | Gateshead | `E08000037` | NE | £2578 | 76 |
| 9 | Hartlepool | `E06000001` | NE | £2499 | 76 |
| 10 | Newark and Sherwood | `E07000175` | EM | £2582 | 76 |
| 11 | Surrey Heath | `E07000214` | SE | £2468 | 75 |
| 12 | Oldham | `E08000004` | NW | £2459 | 74 |
| 13 | Guildford | `E07000209` | SE | £2429 | 73 |
| 14 | South Gloucestershire | `E06000025` | SW | £2428 | 73 |
| 15 | West Oxfordshire | `E07000181` | SE | £2444 | 73 |
| 16 | Broxtowe | `E07000172` | EM | £2516 | 72 |
| 17 | Bury | `E08000002` | NW | £2415 | 72 |

**Full 96 (priority order):**

1. `E06000017` — **Rutland** (EM) · bite 82
2. `E07000178` — **Oxford** (SE) · bite 80
3. `E07000064` — **Rother** (SE) · bite 80
4. `E06000047` — **Durham** (NE) · bite 79
5. `E07000062` — **Hastings** (SE) · bite 79
6. `E07000173` — **Gedling** (EM) · bite 77
7. `E07000043` — **North Devon** (SW) · bite 77
8. `E08000037` — **Gateshead** (NE) · bite 76
9. `E06000001` — **Hartlepool** (NE) · bite 76
10. `E07000175` — **Newark and Sherwood** (EM) · bite 76
11. `E07000214` — **Surrey Heath** (SE) · bite 75
12. `E08000004` — **Oldham** (NW) · bite 74
13. `E07000209` — **Guildford** (SE) · bite 73
14. `E06000025` — **South Gloucestershire** (SW) · bite 73
15. `E07000181` — **West Oxfordshire** (SE) · bite 73
16. `E07000172` — **Broxtowe** (EM) · bite 72
17. `E08000002` — **Bury** (NW) · bite 72
18. `E08000021` — **Newcastle upon Tyne** (NE) · bite 72
19. `E06000016` — **Leicester** (EM) · bite 71
20. `E07000215` — **Tandridge** (SE) · bite 70
21. `E07000115` — **Tonbridge and Malling** (SE) · bite 70
22. `E06000037` — **West Berkshire** (SE) · bite 70
23. `E07000202` — **Ipswich** (E) · bite 69
24. `E07000228` — **Mid Sussex** (SE) · bite 69
25. `E09000027` — **Richmond upon Thames** (L) · bite 69
26. `E07000222` — **Warwick** (WM) · bite 69
27. `E06000008` — **Blackburn with Darwen** (NW) · bite 68
28. `E08000022` — **North Tyneside** (NE) · bite 68
29. `E06000027` — **Torbay** (SW) · bite 68
30. `E06000049` — **Cheshire East** (NW) · bite 67
31. `E07000035` — **Derbyshire Dales** (EM) · bite 67
32. `E07000208` — **Epsom and Ewell** (SE) · bite 67
33. `E07000080` — **Forest of Dean** (SW) · bite 67
34. `E07000146` — **King's Lynn and West Norfolk** (E) · bite 67
35. `E07000135` — **Oadby and Wigston** (EM) · bite 67
36. `E06000051` — **Shropshire** (WM) · bite 67
37. `E07000012` — **South Cambridgeshire** (E) · bite 67
38. `E07000213` — **Spelthorne** (SE) · bite 67
39. `E08000033` — **Calderdale** (YH) · bite 66
40. `E06000056` — **Central Bedfordshire** (E) · bite 66
41. `E07000145` — **Great Yarmouth** (E) · bite 66
42. `E09000016` — **Havering** (L) · bite 66
43. `E07000192` — **Cannock Chase** (WM) · bite 65
44. `E07000079` — **Cotswold** (SW) · bite 64
45. `E07000037` — **High Peak** (EM) · bite 64
46. `E07000038` — **North East Derbyshire** (EM) · bite 64
47. `E07000149` — **South Norfolk** (E) · bite 64
48. `E07000242` — **East Hertfordshire** (E) · bite 63
49. `E07000138` — **Lincoln** (EM) · bite 63
50. `E07000139` — **North Kesteven** (EM) · bite 63
51. `E07000103` — **Watford** (E) · bite 63
52. `E07000144` — **Broadland** (E) · bite 62
53. `E07000099` — **North Hertfordshire** (E) · bite 62
54. `E07000198` — **Staffordshire Moorlands** (WM) · bite 62
55. `E07000077` — **Uttlesford** (E) · bite 62
56. `E07000237` — **Worcester** (WM) · bite 62
57. `E07000234` — **Bromsgrove** (WM) · bite 61
58. `E07000132` — **Hinckley and Bosworth** (EM) · bite 61
59. `E06000061` — **North Northamptonshire** (EM) · bite 61
60. `E08000023` — **South Tyneside** (NE) · bite 61
61. `E07000197` — **Stafford** (WM) · bite 61
62. `E07000083` — **Tewkesbury** (SW) · bite 61
63. `E07000067` — **Braintree** (E) · bite 60
64. `E07000096` — **Dacorum** (E) · bite 60
65. `E09000014` — **Haringey** (L) · bite 60
66. `E07000236` — **Redditch** (WM) · bite 60
67. `E08000018` — **Rotherham** (YH) · bite 60
68. `E06000010` — **Kingston upon Hull** (YH) · bite 59
69. `E06000031` — **Peterborough** (E) · bite 59
70. `E07000141` — **South Kesteven** (EM) · bite 59
71. `E07000243` — **Stevenage** (E) · bite 59
72. `E07000076` — **Tendring** (E) · bite 59
73. `E07000036` — **Erewash** (EM) · bite 58
74. `E07000034` — **Chesterfield** (EM) · bite 57
75. `E07000085` — **East Hampshire** (SE) · bite 57
76. `E07000039` — **South Derbyshire** (EM) · bite 57
77. `E06000020` — **Telford and Wrekin** (WM) · bite 57
78. `E07000196` — **South Staffordshire** (WM) · bite 56
79. `E08000009` — **Trafford** (NW) · bite 56
80. `E07000220` — **Rugby** (WM) · bite 55
81. `E07000221` — **Stratford-on-Avon** (WM) · bite 55
82. `E07000093` — **Test Valley** (SE) · bite 55
83. `E07000235` — **Malvern Hills** (WM) · bite 54
84. `E09000024` — **Merton** (L) · bite 54
85. `E07000128` — **Wyre** (NW) · bite 54
86. `E07000084` — **Basingstoke and Deane** (SE) · bite 52
87. `E09000006` — **Bromley** (L) · bite 51
88. `E09000009` — **Ealing** (L) · bite 51
89. `E07000073` — **Harlow** (E) · bite 51
90. `E09000019` — **Islington** (L) · bite 50
91. `E07000238` — **Wychavon** (WM) · bite 50
92. `E09000002` — **Barking and Dagenham** (L) · bite 49
93. `E06000040` — **Windsor and Maidenhead** (SE) · bite 39
94. `E09000001` — **City of London** (L) · bite 27
95. `E09000032` — **Wandsworth** (L) · bite 27
96. `E09000020` — **Kensington and Chelsea** (L) · bite 22

> Machine-readable list: `requests/2026-09-27_unknown-trigger-councils.csv` (now sorted by bite desc). Loop the template over `la`+`ons`.


---

## Section 2 — finance / premium term gaps (specific flagged councils)

```
For [COUNCIL] (ONS [ONS]), confirm for 2025/26:
1. Long-term empty homes premium — trigger (1 or 2 years) and rates at 1/5/10 years.
2. Second-home premium — adopted? from what date? what rate?
3. Any empty-homes loan or grant a BUYER of an empty home could use (amount, term, interest, security, strings such as let-to-council/nomination/clawback, currently open?).
Use the council's own pages / linked PDFs. Give exact https URLs and a short exact quote for each of (1)-(3).
Answer:
ONS: [ONS]
Council: [name]
LTE_trigger: [1 year / 2 years / unclear]
LTE_rates_1_5_10: [e.g. 100/200/300 %]
Second_home_premium: [Yes+rate+date / No / unclear]
Buyer_scheme: [describe or 'none found']
Scheme_strings: [let-back years / nomination / clawback / none]
Scheme_open: [open / closed / suspended / unclear]
Source_URLs: [https URLs]
Evidence_quotes: ["...","..."]
```

Run for: **Hart** `E07000089`, **Surrey Heath** `E07000214`, **North Lincolnshire** `E06000013`, **Spelthorne** `E07000213`, **Bracknell Forest** `E06000036`, **Woking** `E07000217`, **Guildford** `E07000209`, **Barnsley** `E08000016` (find the empty-home grant terms PDF), **Newcastle upon Tyne** `E08000021` (find 'Grant Scheme 1: Empty Properties').


---

## Section 3 — the other dead-ends

### 3a. Bona vacantia / Treasury Solicitor auction lots
```
Do UK residential property auctions ever list lots sold "by order of the Treasury Solicitor" or the Government Legal Department / Bona Vacantia Division? Which auction houses handle Crown / bona vacantia / dissolved-company property? Link at least one real past catalogue lot (with URL) showing this wording. Give auction house, lot description, date, and URL. If none can be found, say so plainly.
```

### 3b. VAT tribunal case law on empty-period evidence (5% / zero rate)
```
Find UK First-tier Tribunal (Tax) or Upper Tribunal decisions on the 5% reduced or zero VAT rate for renovating dwellings empty 2+ or 10+ years - specifically disputes over what EVIDENCE proves the empty period (e.g. Empty Property Officer letters, council tax records). Give case name, neutral citation, year, one-line summary of the evidence issue, and a URL. List each case separately.
```

### 3c. ICO enforcement on reusing published-notice data for marketing
```
Any ICO enforcement actions, decision notices or reprimands about organisations reusing PUBLICLY PUBLISHED data (Gazette statutory notices, insolvency/probate/deceased-estate notices, land/company registers) for DIRECT MARKETING under UK GDPR or PECR? Give organisation, date, outcome, one-line summary, and URL to the ICO decision/press release. If none specific exist, give the nearest analogous cases.
```

### 3d. LAHF per-council allocations
```
Provide a per-council breakdown of Local Authority Housing Fund (LAHF) allocations in England, all rounds (1-4). For each council: total allocated and which round(s). Cite official gov.uk / MHCLG sources. If no single table exists, give the best official round pages plus any reputable aggregation, with URLs.
```

### 3e. FixMyStreet report-data reuse licence
```
Under what licence can FixMyStreet (mySociety) REPORT DATA (not the AGPL software) be reused, including for a commercial product - OGL, Creative Commons, or bespoke? Quote mySociety's own terms/FAQ with the URL.
```

### 3f. Policy in Practice 'Missing Out 2026' (F12 re-check)
```
Has Policy in Practice published its 'Missing Out' report for 2026 (unclaimed benefits / Council Tax Support, Great Britain)? If so, give the headline unclaimed totals (total and Council Tax Support), publication date, and URL.
```


---

## Section 4 — merge-back contract

Hand back the Section-1 CSV rows and Section 2-3 answers. I will: (1) key on `ons`, and update `trigger`/rates/second-home fields in `data/premium_pressure_2025.csv` **only where `source_url` is the council's own domain**, re-run the bite score, and report which councils moved off `unknown`; (2) fold finance terms into the Brief 4 report, dropping `(verify)`/`[secondary]` flags where a primary URL confirms them; (3) add real VAT/ICO cases to the Brief 3 legal items and the auction finding to the bona-vacantia note. `unclear` rows and non-council-domain sources stay flagged, never silently merged. Per the validation rule, a blank rate is treated as `unclear`, never as 'no premium'.
