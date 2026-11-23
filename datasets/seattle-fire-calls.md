# [Your decision question, in your words. It ends with a question mark.]

## Who decides what
[One or two sentences, your words. Name the job (Seattle Fire Department operations planner) and the decision.]

## Data
- Publisher: City of Seattle, Seattle Fire Department (data.seattle.gov)
- Link: https://data.seattle.gov/d/kzjm-xkqj
- Date accessed: [the day you downloaded the file]
- License or terms: Public Domain (license field on the portal metadata)
- Repo rule: LINK ONLY

## What one row means
[One sentence, your words.]

## What I did in my tool (Excel or Tableau)
- Columns I kept: type, datetime, incident_number, plus a new Hour column (the hour of datetime, 0 to 23)
- Filters: datetime from January 1 through June 30, 2025 (set in the download link); in the pivot, type = Aid Response, Auto Fire Alarm, Medic Response and Triaged Incident only
- Pivot: rows Hour, columns type, values Count of incident_number
- Rows after my filters: 41,471
- Check pivot: I expected 41,471 and found 41,471
- Pivot file: analysis/seattle-fire-calls-pivot.csv

## What the numbers show
```
Count of incident_number	Column Labels				
Row Labels	Aid Response	Auto Fire Alarm	Medic Response	Triaged Incident	Grand Total
0	1008	112	154	124	1398
1	875	84	136	129	1224
2	743	88	104	71	1006
3	645	85	111	64	905
4	582	73	130	56	841
5	674	92	131	66	963
6	736	103	132	501	1472
7	908	123	177	112	1320
8	1185	165	234	168	1752
9	1286	180	299	141	1906
10	1448	189	332	176	2145
11	1529	242	321	135	2227
12	1508	219	307	155	2189
13	1589	173	324	163	2249
14	1621	200	266	165	2252
15	1588	155	281	161	2185
16	1651	155	302	201	2309
17	1536	155	281	179	2151
18	1465	190	275	180	2110
19	1520	158	250	157	2085
20	1382	156	239	138	1915
21	1238	144	202	146	1730
22	1217	134	188	146	1685
23	1077	97	163	115	1452
Grand Total	29011	3472	5339	3649	41471
```

## My finding
From January 1 through June 30, 2025, Seattle Fire Department’s busiest hour for Aid Response calls was 4:00–4:59 p.m., with 1,651 dispatches.

## What this data cannot show
[One sentence, your words. Name something your pivot does not tell the reader and why that matters for the decision.]

## What I checked
[One or two sentences, your words: what your LLM tested, your expected and found counts, and anything you checked or corrected.]

## Number trail
See analysis/number-trail.md
