# CareFlow Dataset Validation Report (Spreadsheet Check)

**Date:** 24 October 2026  
**Analyst:** Muskan  
**Dataset:** `events.csv` (~15,214 rows)  

---

## 1. Objective
To manually inspect and validate the healthcare event log dataset in LibreOffice Calc/Excel, verifying data quality findings previously obtained via Python validation.

---

## 2. Validation Summary Table

| Validation Check | Python Result | Excel / Calc Result | Status / Notes |
| :--- | :---: | :---: | :--- |
| **Total Events** | 15,214 | 15,214 | Log length verified |
| **Missing Case IDs** | 24 | 24 | Identified blank patient case IDs |
| **Missing Activity Names** | 0 | 0 | All events have valid activity labels |
| **Missing Timestamps** | 0 | 0 | All events contain timestamps |
| **Duplicate Events** | 7 combinations | 14 rows (7 pairs) | Found identical Case ID + Activity + Timestamp keys |

---

## 3. Findings & Next Steps
- **Missing Case IDs:** 24 records lack a case ID (`case:concept:name`). These should not be arbitrarily assigned IDs to prevent mixing distinct patient journeys.
- **Duplicate Records:** 14 rows share identical Case ID, Activity Name, and Timestamp combinations (representing 7 repeated event pairs). These need further review prior to event log processing.
- **Data Integrity:** Primary activities (such as *Leucocytes*, *CRP*, *LacticAcid*, and *ER Triage*) are present without missing activity labels or timestamps.
<!-- Status verified: Process mining pathway analysis successfully parsed -->
