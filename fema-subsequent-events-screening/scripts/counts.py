"""Basic counts for the FEMA Disaster Declarations Summaries CSV.

Usage: python scripts/counts.py path/to/DisasterDeclarationsSummaries.csv [STATE]

Prints total rows (one row = one designated area within one declaration),
distinct declarations, and blank / zero counts for the columns the screen uses.
If a state code is given (e.g. PA), also prints the same counts for that state.
Blank means missing, not zero.
"""
import csv
import sys

COLUMNS = ["femaDeclarationString", "state", "declarationType", "declarationDate",
           "incidentType", "declarationTitle", "incidentBeginDate", "incidentEndDate",
           "fipsCountyCode", "designatedArea"]


def summarize(rows, label):
    print(f"== {label} ==")
    print("rows (designated areas):", len(rows))
    print("distinct declarations:", len({r["femaDeclarationString"] for r in rows}))
    print("statewide rows (fipsCountyCode 000):", sum(r["fipsCountyCode"] == "000" for r in rows))
    for c in COLUMNS:
        blank = sum((r.get(c) or "").strip() == "" for r in rows)
        zero = sum((r.get(c) or "").strip() == "0" for r in rows)
        print(f"  {c}: blank {blank}, zero {zero}")
    dates = sorted(r["declarationDate"][:10] for r in rows if r["declarationDate"])
    if dates:
        print("declarationDate range:", dates[0], "to", dates[-1])
    print()


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    with open(sys.argv[1], newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    summarize(rows, "all rows")
    if len(sys.argv) > 2:
        st = sys.argv[2].upper()
        summarize([r for r in rows if r["state"] == st], f"state = {st}")


if __name__ == "__main__":
    main()
