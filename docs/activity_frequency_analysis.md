\# CareFlow: Activity Frequency Analysis



\*\*Date:\*\* 25 October 2026



\## Objective

Analyze the healthcare event log using LibreOffice Calc to understand the frequency of recorded clinical activities.



\## Work Completed

\- Created a Pivot Table using `concept:name` as the activity field.

\- Configured the Data Field to use Count.

\- Sorted activity frequencies to identify commonly recorded activities.

\- Created a `Process Analysis` sheet to summarize dataset metrics and initial findings.



\## Reference Findings

Previous Python validation reported the following activity counts:



| Activity | Event Count |

|---|---:|

| Leucocytes | 3,383 |

| CRP | 3,262 |

| LacticAcid | 1,466 |

| Admission NC | 1,182 |

| ER Triage | 1,053 |



These are reference values from the earlier Python analysis and should be cross-checked against the Pivot Table.



\## Tools Used

\- LibreOffice Calc

\- Pivot Tables

\- Python and Pandas for reference validation

\- Git and GitHub



\## Next Steps

\- Verify the Pivot Table counts.

\- Complete the process analysis summary.

\- Examine chronological patient activity sequences.

\- Investigate repeated activities and potential process deviations.



\## Conclusion

Activity frequency analysis is an initial step toward understanding healthcare workflows. Further sequence and timestamp analysis is needed before identifying potential bottlenecks.



