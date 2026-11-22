"""Apply the reversal sentence to a filled-in pilot log.

Usage: python scripts/pilot_summary.py inputs/pilot_log_illustrative.csv

Reversal sentence (student's, threshold PLANNED): at least one new, specific question for
management about potential facility damage, service interruptions, or significant costs
across five completed reviews. If the log shows zero such questions, recommend keeping the
standard subsequent-events inquiry as the sole routine step.

Column new_specific_question_for_management: Y or N. Blank means not yet filled in.
The repo copy is a blank template: real pilot results are confidential and are not published.
"""
import csv
import sys

THRESHOLD = 1        # planned
REVIEWS_PLANNED = 5  # planned


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    with open(sys.argv[1], newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    filled = [r for r in rows if r["new_specific_question_for_management"].strip()]
    yes = sum(r["new_specific_question_for_management"].strip().upper() == "Y" for r in filled)
    minutes = [float(r["minutes_added"]) for r in rows if r["minutes_added"].strip()]
    print(f"Reviews in log: {len(rows)}; filled in: {len(filled)} of {REVIEWS_PLANNED} planned")
    if len(filled) < REVIEWS_PLANNED:
        print("Result: NOT YET TESTABLE - fill in all planned reviews before applying the reversal sentence.")
        return
    print(f"New specific questions for management: {yes} (threshold: at least {THRESHOLD})")
    if minutes:
        print(f"Minutes added: total {sum(minutes):g}, average {sum(minutes)/len(minutes):.1f} per review")
    if yes >= THRESHOLD:
        print("Result: threshold met - the reversal condition is not triggered (next step not yet specified by the student).")
    else:
        print("Result: threshold not met - recommend keeping the standard inquiry as the sole routine step.")


if __name__ == "__main__":
    main()
