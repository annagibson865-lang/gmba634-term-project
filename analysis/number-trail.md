# Number trail

Every number in my findings has a row here. Years and dates do not need a row.

| Page | Number or range | Dataset | Filter | Pivot rows / columns / values | Where in your tool (sheet and cell, or Tableau worksheet) |
|---|---|---|---|---|---|
| datasets/chicago-food-inspections.md | 4,495 | Chicago food inspections (City of Chicago) | inspection_type = Canvass, License; results = Fail, Pass, Pass w/ Conditions; inspection dates after 2024-01-01 | rows facility_type, columns results, values Count of inspection_id (Restaurant row, Fail column) | sheet Pivot, cell B104 |
| datasets/chicago-food-inspections.md | 19,211 | Chicago food inspections (City of Chicago) | inspection_type = Canvass, License; results = Fail, Pass, Pass w/ Conditions; inspection dates after 2024-01-01 | rows facility_type, columns results, values Count of inspection_id (Restaurant row, Grand Total column) | sheet Pivot, cell E104 |
| datasets/chicago-food-inspections.md | 23.4% | Chicago food inspections (City of Chicago) | inspection_type = Canvass, License; results = Fail, Pass, Pass w/ Conditions; inspection dates after 2024-01-01 | rows facility_type, columns results, values Count of inspection_id shown as % of Row Total (Restaurant row, Fail column, 23.40%) | sheet Pivot - Percent, cell B104 |
| datasets/seattle-fire-calls.md | 1,651 | Seattle fire 911 dispatches (City of Seattle) | datetime January 1 through June 30, 2025; type = Aid Response, Auto Fire Alarm, Medic Response, Triaged Incident | rows Hour, columns type, values Count of incident_number (hour 16 row, Aid Response column) | sheet Pivot, cell B21 |
