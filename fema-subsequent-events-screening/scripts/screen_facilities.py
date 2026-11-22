"""Screen facility locations against FEMA disaster declarations for a subsequent-events review.

Usage:
  python scripts/screen_facilities.py DECLARATIONS.csv FACILITIES.csv YEAR_END REPORT_DATE OUTPUT.csv

  DECLARATIONS.csv  FEMA Disaster Declarations Summaries v2 CSV (or the illustrative test file)
  FACILITIES.csv    columns: facility_id, facility_name, facility_type, state, county
  YEAR_END          audit year-end, YYYY-MM-DD (review period starts the next day)
  REPORT_DATE       planned report date, YYYY-MM-DD (review period ends on this day, inclusive)

A facility is flagged when a declaration row for its state covers its county, or is a
statewide designation (fipsCountyCode 000), AND either:
  - the incident dates overlap the review period, or
  - the incident ended on or before year-end but the declaration date is in the review period.
A blank incidentEndDate is treated as an ongoing incident (it is noted in the reason).

A match only flags a facility for follow-up with management. It does not show that the
facility was damaged.
"""
import csv
import sys
from datetime import date, timedelta


def d(text):
    text = (text or "").strip()
    return date.fromisoformat(text[:10]) if text else None


def county_name(area):
    return area.replace("(County)", "").strip().lower()


def main():
    if len(sys.argv) != 6:
        sys.exit(__doc__)
    decl_path, fac_path, ye, rd, out_path = sys.argv[1:]
    year_end, report_date = d(ye), d(rd)
    start = year_end + timedelta(days=1)

    with open(fac_path, newline="", encoding="utf-8-sig") as f:
        facilities = list(csv.DictReader(f))
    states = {fac["state"].upper() for fac in facilities}

    with open(decl_path, newline="", encoding="utf-8-sig") as f:
        decls = [r for r in csv.DictReader(f) if r["state"].upper() in states]

    out_rows = []
    for fac in facilities:
        matches = []
        for r in decls:
            if r["state"].upper() != fac["state"].upper():
                continue
            statewide = r["fipsCountyCode"] == "000"
            if not statewide and county_name(r["designatedArea"]) != fac["county"].strip().lower():
                continue
            begin, end, declared = d(r["incidentBeginDate"]), d(r["incidentEndDate"]), d(r["declarationDate"])
            reasons = []
            if begin and begin <= report_date and (end is None or end >= start):
                reasons.append("Incident overlaps review period")
                if end is None:
                    reasons.append("Incident end date blank (treated as ongoing)")
            elif end is not None and end < start and declared and start <= declared <= report_date:
                reasons.append("Pre-year-end incident, declaration during review period")
            if not reasons:
                continue
            if statewide:
                reasons.append("Statewide designation")
            matches.append((r, reasons))

        base = {k: fac[k] for k in ("facility_id", "facility_name", "state", "county")}
        if not matches:
            out_rows.append({**base, "result": "No FEMA match found"})
        for r, reasons in matches:
            out_rows.append({**base, "result": "FEMA match found",
                             "disaster_number": r["femaDeclarationString"],
                             "declaration_title": r["declarationTitle"],
                             "incident_type": r["incidentType"],
                             "incident_begin": r["incidentBeginDate"][:10],
                             "incident_end": (r["incidentEndDate"] or "")[:10],
                             "declaration_date": r["declarationDate"][:10],
                             "designated_area": r["designatedArea"],
                             "match_reason": "; ".join(reasons)})

    fields = ["facility_id", "facility_name", "state", "county", "result", "disaster_number",
              "declaration_title", "incident_type", "incident_begin", "incident_end",
              "declaration_date", "designated_area", "match_reason"]
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out_rows)

    flagged = {row["facility_id"] for row in out_rows if row["result"] == "FEMA match found"}
    declarations = {row["disaster_number"] for row in out_rows if row["result"] == "FEMA match found"}
    print(f"Review period: {start} to {report_date}")
    print(f"Distinct declarations matching at least one facility: {len(declarations)}")
    print(f"Facilities with at least one match: {len(flagged)} of {len(facilities)}")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
