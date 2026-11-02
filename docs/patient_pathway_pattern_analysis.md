\# Patient Pathway Pattern Analysis



\## 1. Objective

To analyze patient activity sequences and identify common pathway patterns and variations in the number of activities recorded for each patient case.



\## 2. Methodology

\- Loaded the hospital event dataset from `data/events.csv`.

\- Converted event timestamps into datetime format.

\- Removed records with missing case IDs, activity names, or timestamps.

\- Sorted activities by patient case and timestamp.

\- Grouped activities into individual patient pathways.

\- Identified the most common complete activity sequences.

\- Summarized the number of activities recorded for each patient case.



\## 3. Analysis Results



| Metric | Result |

|---|---:|

| Total patient cases analyzed | 1,049 |

| Unique pathway patterns | 845 |

| Most common pathway | ER Registration → ER Triage → ER Sepsis Triage |

| Cases following the most common pathway | 35 |

| Minimum activities in a pathway | 3 |

| Maximum activities in a pathway | 185 |



\## 4. Common Patient Pathways



The most frequently observed complete pathways were:



1\. ER Registration → ER Triage → ER Sepsis Triage — 35 cases.

2\. ER Registration → ER Triage → ER Sepsis Triage → Leucocytes → CRP — 24 cases.

3\. ER Registration → ER Triage → ER Sepsis Triage → CRP → Leucocytes — 22 cases.

4\. ER Registration → ER Triage → ER Sepsis Triage → CRP → LacticAcid → Leucocytes → IV Liquid → IV Antibiotics — 13 cases.

5\. ER Registration → ER Triage → ER Sepsis Triage → Leucocytes → CRP → LacticAcid — 11 cases.



The results show variations in the order and number of diagnostic and treatment-related activities after the initial registration and triage stages.



\## 5. Pathway Length Observations



\- 35 cases contained 3 activities.

\- 100 cases contained 8 activities.

\- 95 cases contained 13 activities.

\- 81 cases contained 12 activities.

\- One case contained 185 activities.



The wide variation in pathway length indicates that patient cases have different recorded activity volumes. The case with 185 activities may require further investigation to understand repeated events and the overall case timeline.



\## 6. Generated Analysis Files



The following files were generated:



\- `data/patient\_pathway\_sequences.csv`

\- `data/common\_patient\_pathways.csv`

\- `data/patient\_pathway\_length\_summary.csv`



These files contain individual patient sequences, common complete pathways, and pathway length summaries.



\## 7. Conclusion



Patient pathway analysis identified 845 distinct complete activity sequences across 1,049 cases. The most common sequence was the initial registration and triage pathway, observed in 35 cases.



The analysis provides a foundation for understanding variations in patient activity sequences and can support further process investigation and dashboard development.



\## 8. Limitations



\- Exact complete sequences can differ even when patients share similar initial activities.

\- A high activity count does not automatically indicate an error or inefficient care.

\- The analysis is based on recorded event sequences and does not establish clinical appropriateness or causation.

\- Activities with identical timestamps may have an uncertain relative order.



