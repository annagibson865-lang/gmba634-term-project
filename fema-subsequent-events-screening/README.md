# Screening Client Facilities for FEMA Disasters During Subsequent-Events Review

A Python screen that flags an audit client's facilities located in FEMA-declared disaster areas between year-end and the planned report date, so the engagement team has a specific event to ask management about during subsequent-events review. Class project for GMBA634 (this folder of the gmba634-term-project repo); client and facilities are fictional.

## The case in brief
- **Decider:** the engagement manager (role-play scenario; not confirmed with a real manager).
- **Ask:** By the start of the next audit wrap-up, I am asking the engagement manager to approve a small retrospective pilot to test whether the FEMA screen would have prompted additional follow-up alongside the standard subsequent-events inquiry.
- **Claim:** From January 1 through March 31, 2026, the FEMA screen matched zero qualifying declarations and flagged zero of five illustrative facilities, leaving the engagement manager to decide by the start of the next audit wrap-up whether to approve a pilot to test whether the screen adds value.
- **What would change my mind:** see [case/scr-worksheet.md](case/scr-worksheet.md), Box 6.

## Data source
- Federal Emergency Management Agency (FEMA), OpenFEMA Dataset: Disaster Declarations Summaries - v2. Downloaded as CSV from https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries.csv on November 19, 2026 (file refreshed by FEMA on November 13, 2026). Documentation: https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2
- One row = one designated area (county or statewide) within one declaration. The raw file is **not** included in this repo; download it from the link above and save it as `data/declarations.csv` inside this folder.
- Facility locations, year-end (December 31, 2025) and planned report date (March 31, 2026) are **illustrative**: a fictional local government with five facilities in real Pennsylvania counties (Erie, Crawford, Mercer, Venango, Warren).

## How the screen works
A facility is flagged when a FEMA declaration in its state covers its county or is a statewide designation (county code `000`), and either:
1. the incident dates overlap the review period (day after year-end through the planned report date), or
2. the incident ended on or before year-end but the declaration date falls in the review period ("Pre-year-end incident, declaration during review period").

Statewide matches are labelled "Statewide designation". A match only flags a facility for follow-up with management; it does not show that the facility was damaged. The screen cannot see local events that never received a federal declaration, or declarations issued after the report date.

## How to run
Requires Python 3 (standard library only). Run from inside this folder.
```
cd fema-subsequent-events-screening
python scripts/counts.py data/declarations.csv PA
python scripts/screen_facilities.py data/declarations.csv inputs/facilities_illustrative.csv 2025-12-31 2026-03-31 outputs/screen_results_fema_2026Q1.csv
python scripts/screen_facilities.py inputs/test_declarations_illustrative.csv inputs/facilities_illustrative.csv 2025-12-31 2026-03-31 outputs/screen_results_test_illustrative.csv
python scripts/pilot_summary.py inputs/pilot_log_illustrative.csv
```

## Files
| File | What it is |
|---|---|
| [case/project-brief.md](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/fema-subsequent-events-screening/case/project-brief.md) | Project brief: decider, decision, data and status labels |
| [case/claim-and-ask.md](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/fema-subsequent-events-screening/case/claim-and-ask.md) | Claim, ask, the pivot behind them, and the skeptic test |
| [case/scr-worksheet.md](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/fema-subsequent-events-screening/case/scr-worksheet.md) | SCR boxes 1–6 |
| [ai-component/project-instructions.md](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/fema-subsequent-events-screening/ai-component/project-instructions.md) | Instructions and guardrails given to the AI |
| [scripts/counts.py](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/fema-subsequent-events-screening/scripts/counts.py) | Row, declaration and blank/zero counts |
| [scripts/screen_facilities.py](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/fema-subsequent-events-screening/scripts/screen_facilities.py) | The facility screen |
| [scripts/pilot_summary.py](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/fema-subsequent-events-screening/scripts/pilot_summary.py) | Applies the reversal sentence to a filled-in pilot log |
| [inputs/facilities_illustrative.csv](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/fema-subsequent-events-screening/inputs/facilities_illustrative.csv) | Five fictional facilities (ILLUSTRATIVE) |
| [inputs/test_declarations_illustrative.csv](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/fema-subsequent-events-screening/inputs/test_declarations_illustrative.csv) | Six fictional declarations testing each rule (ILLUSTRATIVE) |
| [inputs/pilot_log_illustrative.csv](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/fema-subsequent-events-screening/inputs/pilot_log_illustrative.csv) | Blank pilot log template (real results are confidential and not published) |
| [outputs/screen_results_fema_2026Q1.csv](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/fema-subsequent-events-screening/outputs/screen_results_fema_2026Q1.csv) | Screen on real FEMA data: 0 of 5 flagged |
| [outputs/screen_results_test_illustrative.csv](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/fema-subsequent-events-screening/outputs/screen_results_test_illustrative.csv) | Screen on the fictional test file (demonstration only, not a finding) |

## Status
- **Measured by the student:** 0 FEMA declarations and 0 of 5 facilities matched for January 1 – March 31, 2026 (Excel; filters in case/claim-and-ask.md).
- **Re-run by the student (GitHub Codespaces, 2026-11-22):** all four scripts, with output matching the AI run: 1,252 PA rows / 64 PA declarations; 0 of 5 facilities flagged on the FEMA file; 5 of 5 on the fictional test file (3 test declarations); pilot log "not yet testable".
- **Illustrative:** facilities, review dates, and the test-file results (3 fictional declarations match, 3 correctly do not). The test results demonstrate the rules; they are not findings.
- **Not done:** the retrospective pilot (proposal only).

## AI use
This is a class project, not paid, employer or client work; the firm and clients are withheld and all client details are fictional. AI use was encouraged by the professor.
- **Claude (Anthropic)** profiled the dataset, wrote the project instructions and the brief from the student's interview answers, wrote and tested the three Python scripts and the illustrative input files, tested the student's claim, ask and SCR boxes, and drafted this README's structure, file list, run instructions and AI-use section, and added the files to GitHub through the student's signed-in browser (the student merges each pull request).
- **Another AI tool** suggested the retrospective-pilot idea; the student wrote the ask in their own words.
- **The student** chose the scenario and screen rules, ran the Excel check, re-ran all four scripts in GitHub Codespaces on 2026-11-22 (output matched), and wrote the claim, ask, SCR boxes and reversal sentence.
