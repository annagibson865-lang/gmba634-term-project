# SCR worksheet (P1.2)

Boxes written by the student; Claude's test notes in italics.

## Box 1 — Situation
During audit wrap-up, the engagement team asks management whether anything happened after year-end that could affect the financial statements. If management identifies a potential issue, the team follows up before dating the auditor's report.

*Test: OK — describes current practice the decider would agree with; no complication or answer yet.*

## Box 2 — Complication
Management may give a general answer to the subsequent-events inquiry and overlook a storm near one of its facilities, especially if the impact is still being assessed. Without a specific event or location to ask about, the engagement team may miss an opportunity to follow up before dating the report.

*Test: OK — names the gap in the Situation. "May" is a belief, not measured: this is the HYPOTHESIS the pilot tests; keep "may".*

## Box 3 — Question
Should the engagement manager approve a small retrospective pilot by the start of the next audit wrap-up to test whether the FEMA screen would have prompted follow-up on potential facility impacts that the standard subsequent-events inquiry missed?

*Test: OK — one yes/no question; same decider, decision and deadline as the ask; follows from Box 2.*

## Box 4 — Resolution / answer
Yes, the engagement manager should approve a small retrospective pilot by the start of the next audit wrap-up. The illustrative review flagged zero of five facilities, and one period is too little to judge whether the screen adds value. The pilot would test whether the screen identifies events worth asking management about that the standard inquiry missed.

*Test: OK (revised once) — answers Box 3; reason now follows from the evidence.*

## Box 5 — Evidence
- Measured in Excel using public FEMA data and illustrative facilities. From January 1 through March 31, 2026, the screen matched 0 distinct FEMA declarations and flagged 0 of 5 facilities. I filtered to Pennsylvania and checked Erie, Crawford, Mercer, Venango, and Warren counties, plus statewide designations (county code `000`). A record qualified if its incident dates overlapped the review period or its declaration date fell within it.
- Fictional test cases, verified by rerunning the script myself. I confirmed that the script flags a facility when a pre-year-end incident is declared during the review period and flags all five facilities when a qualifying statewide Pennsylvania designation appears.
- Evidence still needed. The Excel check covers one illustrative period. I haven't measured whether the screen would have changed the team's follow-up on a completed engagement or how much time it would add.

Hypothesis. The FEMA screen may identify a specific event worth asking management about that the standard subsequent-events inquiry did not surface. The retrospective pilot would test that.

*Test: OK — facts and beliefs separated, each with status. Test-file result re-run by the student in GitHub Codespaces on 2026-11-22 (5 of 5 flagged, matching the AI run); the student checked the match_reason column (Crawford pre-year-end row; statewide rows for all five). Bullet 2 revised by the student 2026-11-22.*

## Box 6 — What would change my mind (reversal sentence)
My planned threshold is at least one new, specific question for management about potential facility damage, service interruptions, or significant costs across five completed reviews. If the pilot log of FEMA flags and prior management responses shows zero such questions, I would recommend that the engagement manager keep the standard subsequent-events inquiry as the sole routine step.

*Test: OK — number (≥1 new specific question across 5 completed reviews, PLANNED threshold); where (pilot log of FEMA flags and prior management responses); change it forces (keep the standard inquiry as the sole routine step). Time added is not part of the threshold — the student's choice.*
