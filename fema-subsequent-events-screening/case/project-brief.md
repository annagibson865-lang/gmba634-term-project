# Project brief — FEMA subsequent-events screening

Status: draft from the student's interview answers (2026-11-19 to 2026-11-21). Words in quotes are the student's.

## Me and my domain
Staff accountant on the audit side of a public accounting firm (firm and clients: withheld).

## The situation (anonymised)
In audit work, the student helps review subsequent events by asking management whether anything happened after year-end that could affect the financial statements. Scenario: a severe storm occurs after year-end near a facility operated by a local government client. The student would use FEMA disaster declaration data to check whether the facility's county was included and when the storm occurred, then ask management whether the facility was damaged, whether services were interrupted, and whether there were significant repair costs. "The declaration would help me decide where to follow up, and the client's records would help the engagement team assess whether the impact warranted disclosure."

## Who decides, and what
- **Decider:** the engagement manager (role).
- **Decision (revised 2026-11-21, student's words):** "The engagement manager decides by the start of the next audit wrap-up whether to approve a small retrospective pilot of the FEMA screen. The pilot would test whether the screen surfaces events that warrant follow-up beyond what the standard subsequent-events inquiry already covers."
- **By when:** the start of the next audit wrap-up.
- **Per-engagement context (original interview):** on each engagement, before the auditor's report is dated, the manager decides whether the standard subsequent-events inquiry is sufficient or whether to perform additional procedures (asking management about damage or service interruptions; reviewing repair estimates or insurance claims) to assess whether disclosure is needed.
- Status: **role-play** — the student has not discussed this with a real engagement manager.

## The job to be done (how I know)
- The manager's question: "Did a disaster affect any of the client's facilities between year-end and the planned report date, and do we need to follow up?"
- What they know: where the client's facilities are located; management's responses to the standard subsequent-events inquiry.
- Their time: a few minutes during wrap-up if management confirms facilities were unaffected; longer if management reports damage or interruptions or is unsure.
- How I know: **role-play, not confirmed by a real engagement manager.**

## Data I can use

| Data | Status | Use |
|---|---|---|
| FEMA Disaster Declarations Summaries v2 (CSV, downloaded 2026-11-19 from https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries.csv; lastRefresh 2026-11-13) | Public; measured by FEMA. Student's Excel check: see pivot row below. | Designated county, incident dates, declaration date |
| Five facility locations of a fictional local government in Pennsylvania | ILLUSTRATIVE (real county names: Erie, Crawford, Mercer, Venango, Warren; made-up facilities) — see inputs/facilities_illustrative.csv | Inputs to the screen |
| Year-end (December 31) and planned report date | ILLUSTRATIVE scenario inputs: year-end 2025-12-31, planned report date 2026-03-31 (review period 2026-01-01 to 2026-03-31) | Defines the review period |
| Typical report-dating lag; how often follow-up is needed | Not available — the student will not estimate these | — |
| Pivot: distinct declarations matching ≥1 facility = 0; facilities with ≥1 match = 0 of 5 (review period 2026-01-01 to 2026-03-31, illustrative) | Measured by the student in Excel (2026-11-21): state = PA; designatedArea = Erie, Crawford, Mercer, Venango, Warren; plus fipsCountyCode 000; no dates in the review period. Also AI-run with the same result. | Claim and ask |
| Other profile counts in ai-component/project-instructions.md | AI-run; the student's re-run of counts.py (2026-11-22) confirmed 70,599 rows, 5,286 declarations, 1,617 statewide rows, 623 blank incidentEndDate | Context |
| inputs/facilities_illustrative.csv | ILLUSTRATIVE: five fictional facilities, real PA county names | Screen input |
| inputs/test_declarations_illustrative.csv | ILLUSTRATIVE: six fictional declarations (3 should match, 3 should not) | Shows the flag rules |
| outputs/screen_results_fema_2026Q1.csv | Real FEMA data (0 of 5 flagged); matches the student's Excel check; re-run by the student in GitHub Codespaces 2026-11-22 with the same result | Sample output |
| outputs/screen_results_test_illustrative.csv | ILLUSTRATIVE; re-run by the student 2026-11-22 (5 of 5 flagged, 3 test declarations) | Demonstration only, not a finding |
| inputs/pilot_log_illustrative.csv | Blank template: real pilot results are confidential and will not be published | Pilot proposal |

## The AI idea
A Python script takes the five fictional facility locations, the audit year-end and the planned report date, and matches each facility's county and state to the FEMA declarations. It flags a facility when:
1. any incident dates overlap the period after year-end through the planned report date; or
2. the incident was before year-end but the declaration date falls within the review period — labelled "Pre-year-end incident, declaration during review period", showing both dates; or
3. a statewide Pennsylvania designation (county code 000) meets the date criteria — every PA facility flagged, labelled "Statewide designation".

Output: a table with "FEMA match found" / "No FEMA match found" per facility; for each match: facility, county, disaster name and number, incident dates, declaration date, and the reason for the flag. A match only flags a facility for follow-up; management's response is what shows whether the facility was actually affected.

## Constraints
- Due **2026-11-24**. Interim milestones / freeze window: [ASK ME: confirm with course].
- Tools: Python (matching), Excel (reviewing results), GitHub.
- AI: the professor encourages AI use throughout. AI helps write and troubleshoot the script and drafts the README structure, file list, run instructions and AI-use section. The student writes the claim, ask, SCR boxes, recommendation and reversal sentence; AI may test them for clarity and consistency.
- Illustrative data: facilities and dates labelled illustrative; additional course requirements: [ASK ME: confirm].
- Repo: class repo `gmba634-term-project`, folder `fema-subsequent-events-screening/` (student, 2026-11-22: the project is supposed to be in the class repo). Also published earlier as its own repo. Raw FEMA CSV not committed; linked instead.

## What a hiring manager should conclude
"I want a hiring manager to see that I can take a question that comes up during audit wrap-up and build a tool that helps the team answer it. In this project, I use public FEMA data and Python to flag facilities that may warrant a follow-up with management. I also want them to see how I use AI in my work. I can use it to help build and document the tool, verify the output against the source data, and apply my own judgment about what the results mean for the audit."
(Verifying output against the source: done for the screen — Excel check 2026-11-21 and script re-run in GitHub Codespaces 2026-11-22.)

## Scenario decision (2026-11-21)
Student chose option (a): keep the five counties and the Jan 1 – Mar 31, 2026 review period and report the measured zero. The flag logic will be shown with a separate fictional test file (`test_declarations_illustrative.csv`), labelled illustrative and never mixed with FEMA results. (Option (a) was Claude's recommendation; the student chose it.)

## Pilot direction (2026-11-21)
- The student changed the ask to approving a small retrospective pilot of the FEMA screen alongside the standard inquiry. The pilot idea and wording came from **another AI tool** (student's statement), not from the student or Claude.
- The pilot is a **proposal only**: no real client results go in the repo. The repo shows the design plus the fictional test file.
- New ask sentence: written by the student in their own words (see below).

## Unknowns
- [ASK ME: interim milestones or freeze window?]
- [ASK ME: course requirements for illustrative data?]
- Whether real engagement managers ask this question this way (role-play only).
- FEMA data timing: declarations can come weeks after an incident, and the file reflects only what was declared by its refresh date (2026-11-13).

## Public-safe check
- FEMA data: public, government areas only, no personal data.
- Firm, clients, colleagues: withheld. Facilities: fictional, labelled illustrative.
- No confidential figures used.

## My ask, claim and reversal sentence
(Written by the student in steps P1.1 and P1.2.)
- MY ASK: By the start of the next audit wrap-up, I am asking the engagement manager to approve a small retrospective pilot to test whether the FEMA screen would have prompted additional follow-up alongside the standard subsequent-events inquiry.
- MY CLAIM: From January 1 through March 31, 2026, the FEMA screen matched zero qualifying declarations and flagged zero of five illustrative facilities, leaving the engagement manager to decide by the start of the next audit wrap-up whether to approve a pilot to test whether the screen adds value.
- REVERSAL SENTENCE: My planned threshold is at least one new, specific question for management about potential facility damage, service interruptions, or significant costs across five completed reviews. If the pilot log of FEMA flags and prior management responses shows zero such questions, I would recommend that the engagement manager keep the standard subsequent-events inquiry as the sole routine step. (threshold is PLANNED)
