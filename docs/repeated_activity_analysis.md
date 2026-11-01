\# Repeated Activity Analysis



\## 1. Objective

To identify repeated hospital activities within individual patient cases and understand their frequency across the dataset.



\## 2. Methodology

\- Loaded the original event dataset using Python and Pandas.

\- Converted timestamps into datetime format.

\- Removed records missing essential case IDs or activity names.

\- Grouped records by patient case and activity.

\- Identified activities occurring more than once within the same case.

\- Generated case-level and activity-level summary reports.



\## 3. Analysis Results



\- Total event records analyzed: 15,190

\- Cases with repeated activities: 743

\- Repeated case-activity combinations: 1,860



\### Activity Summary



| Activity | Cases with Repetition | Total Occurrences | Maximum Repetitions |

|---|---:|---:|---:|

| CRP | 691 | 2,942 | 69 |

| Leucocytes | 676 | 3,039 | 74 |

| Admission NC | 312 | 693 | 5 |

| LacticAcid | 171 | 776 | 51 |

| Admission IC | 7 | 14 | 2 |

| ER Triage | 3 | 6 | 2 |



\## 4. Key Observations



1\. CRP was repeated in 691 patient cases.

2\. Leucocytes was repeated in 676 patient cases.

3\. Leucocytes had the highest maximum repetition count, reaching 74 occurrences in one case.

4\. Admission NC appeared repeatedly in 312 cases.

5\. LacticAcid showed repeated occurrences in 171 cases.



These patterns identify activities that may require further investigation.



\## 5. Conclusion



The analysis identified repeated activity patterns across 743 patient cases. CRP and Leucocytes were the most frequently repeated activities across cases.



Repeated activities may reflect routine monitoring, follow-up testing or other clinical processes. Further investigation is needed before interpreting them as workflow inefficiencies.



\## 6. Generated Files



\- `analyze\_repeated\_activities.py`

\- `data/repeated\_activity\_analysis.csv`

\- `data/repeated\_activity\_summary.csv`



\## 7. Tools Used



Python, Pandas, CSV, Git and GitHub.

