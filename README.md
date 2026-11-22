# Checking Nonprofit Clients Against IRS Records

A planned EIN lookup that compares a prospective nonprofit client with public IRS records and flags differences for the engagement partner's accept, defer or decline decision.

## Data source
IRS Exempt Organizations Business Master File Extract (EO BMF), Region 1: Northeast (eo1.csv), downloaded 11/17/2026.
https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf

The raw CSV is not included in this repository. Download it from the link above.
Intake details used in examples are fictional and labelled illustrative.

## Files
- [`case/project-brief.md`](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/case/project-brief.md): project brief
- [`ai-component/project-instructions.md`](https://github.com/annagibson865-lang/gmba634-term-project/blob/main/ai-component/project-instructions.md): the standing instructions I gave my AI assistant
- `counts.py`: counts records, distinct EINs and blank/zero amounts. Run: `python counts.py eo1.csv`
- `pilot_scenarios_illustrative.csv`: 10 fictional intake scenarios for the pilot (times and catches blank until the pilot is run)
- `lookup.py`: exact EIN lookup that flags name, exemption-type and state differences. Run: `python lookup.py eo1.csv pilot_scenarios_illustrative.csv`
- `lookup_results.csv`: output of `lookup.py` on the 10 scenarios
- `pilot_summary.py`: medians and the reversal test. Run: `python pilot_summary.py pilot_results_illustrative.csv`
- `pilot_results_illustrative.csv`: **made-up** pilot times for the class presentation (labelled illustrative; not measured)

## Status
The lookup has been run on the 10 illustrative scenarios. The pilot times in pilot_results_illustrative.csv are **made up** for the class presentation (the course allows made-up data); they were not measured. With those illustrative times: median 187.5 s manual vs 109.5 s AI-assisted, no material discrepancies missed.

## AI use
This is a class project, not paid, employer or client work. Claude (Anthropic) interviewed me to structure the project brief, wrote counts.py, lookup.py and pilot_summary.py, drafted the 10 illustrative scenarios and generated the made-up illustrative pilot times. The ask, hypothesis, reversal sentence and decisions are mine. I have not yet re-run the scripts myself.


## Second project: FEMA subsequent-events screening
A Python screen that flags fictional audit-client facilities in FEMA-declared disaster areas during subsequent-events review. See [fema-subsequent-events-screening/](fema-subsequent-events-screening/) and its README.
