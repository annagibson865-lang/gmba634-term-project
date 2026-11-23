# [Your decision question, in your words. It ends with a question mark.]

## Who decides what
[One or two sentences, your words. Name the job (an adviser to a family) and the decision (buy now or wait a year).]

## Data
- Publisher: Freddie Mac Primary Mortgage Market Survey, distributed by the Federal Reserve Bank of St. Louis (FRED)
- Link: https://fred.stlouisfed.org/series/MORTGAGE30US
- Date accessed: November 22, 2026
- License or terms: The FRED page links its terms (https://fred.stlouisfed.org/legal/#copyright-citation-required) and says the series is copyrighted by Freddie Mac (citation required). I did not read the full terms.
- Repo rule: LINK ONLY

## What one row means
[One sentence, your words.]

## What I did in my tool (Excel or Tableau)
- Columns I kept: observation_date, MORTGAGE30US, Year (a new column, =YEAR of observation_date)
- Filters: deleted the weeks before 2015, so only January 8, 2015 through November 19, 2026 remain
- Pivot: rows Year, columns none, values Average of MORTGAGE30US
- Rows after my filters: 620
- Check pivot: I expected 620 and found 620
- Pivot file: analysis/mortgage-rates-year-pivot.csv

## What the numbers show
```
Average pivot (MORTGAGE30US is the weekly 30-year fixed mortgage rate, in percent)
Row Labels	Average of MORTGAGE30US
2015	3.850576923
2016	3.654038462
2017	3.989807692
2018	4.544615385
2019	3.935769231
2020	3.111698113
2021	2.957692308
2022	5.344038462
2023	6.806730769
2024	6.721153846
2025	6.59509434
2026	6.559565217
Grand Total	4.822629032

Check pivot (number of weekly rates per year)
Row Labels	Count of MORTGAGE30US
2015	52
2016	52
2017	52
2018	52
2019	52
2020	53
2021	52
2022	52
2023	52
2024	52
2025	53
2026	46
Grand Total	620
```

## My finding
In the dataset spanning January 8, 2015, through November 19, 2026, the average 30-year fixed mortgage rate for 2026 through November 19 was 6.56%, lower than the 6.60% average for 2025.

## What this data cannot show
[One sentence, your words. Name something your pivot does not tell the reader and why that matters for the decision.]

## What I checked
[One or two sentences, your words: what D4 tested, your expected and found counts, and what you changed (for example, removing the word "slightly" and the blank row).]

## Number trail
See analysis/number-trail.md
