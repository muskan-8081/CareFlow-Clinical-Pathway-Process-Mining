\# CareFlow: Case-Level Delay Investigation



\## 1. Objective

The objective of this analysis is to investigate unusually long intervals between consecutive healthcare activities at the individual case level.



\## 2. Methodology

Python and Pandas were used to analyze elapsed-time records and identify intervals exceeding 360 minutes (6 hours).



The analysis includes:

\- Case-wise interval investigation

\- Elapsed-time calculation in hours

\- Transition classification

\- Case-level statistical summaries

\- Category-wise investigation summaries



\## 3. Analysis Results



\- Total transitions analyzed: 14,141

\- Intervals exceeding 6 hours: 3,668

\- Unique cases with long intervals: 806



\## 4. Investigation Categories



| Category | Intervals |

|---|---:|

| Other transition | 1,754 |

| Potential return visit | 293 |

| Repeated activity | 887 |

| Transition requiring investigation | 734 |



\## 5. Key Observations



Other transitions represent the largest category of long intervals. Repeated activities and transitions involving Admission NC also require further examination.



Potential return visits have particularly long elapsed intervals, which may represent separate emergency visits rather than continuous hospital waiting.



\## 6. Conclusion



The case-level analysis provides a structured way to identify patient cases and activity transitions requiring further investigation. Long intervals are not automatically confirmed clinical delays; additional case-level and clinical context is necessary.



\## 7. Tools Used

Python, Pandas, CSV, Git and GitHub.

