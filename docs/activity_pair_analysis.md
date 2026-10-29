\# CareFlow: Activity-Pair Analysis



\## Objective

Analyze consecutive clinical activity pairs to understand transition frequency and elapsed-time patterns in patient journeys.



\## Analysis Summary

\- Total transitions analyzed: 14,141

\- Unique activity pairs: 115

\- Minimum frequency used for median-based ranking: 10 transitions per pair



\## Key Findings



\### 1. Most Frequent Transitions

\- Leucocytes → CRP: 1,774 transitions

\- CRP → Leucocytes: 1,443 transitions

\- ER Registration → ER Triage: 970 transitions

\- ER Triage → ER Sepsis Triage: 904 transitions

\- CRP → LacticAcid: 627 transitions



\### 2. Emergency Department Transitions

\- ER Registration → ER Triage had a median elapsed time of approximately 7.9 minutes.

\- ER Triage → ER Sepsis Triage had a median elapsed time of approximately 0.42 minutes.



These values describe the intervals between recorded timestamps and should not automatically be interpreted as complete operational waiting times.



\### 3. Long Intervals

\- Release A → Return ER occurred 276 times and had a median interval of approximately 47.3 days.

\- This pattern may represent a return visit after discharge and should be analyzed separately from within-visit delays.

\- Repeated laboratory activities, including Leucocytes → Leucocytes, also showed long median intervals.



\### 4. Mean Versus Median

Some activity pairs have much higher mean elapsed times than median elapsed times. This indicates that long intervals affect the averages, making medians useful for understanding typical recorded intervals.



\## Limitations

Elapsed time is calculated from consecutive event timestamps. It does not directly measure treatment duration, waiting time, or the cause of a delay. Clinical interpretation requires additional investigation of case sequences and event context.



\## Next Steps

\- Separate return-visit transitions from within-visit transitions where possible.

\- Investigate frequent transitions with consistently long median intervals.

\- Validate unusual intervals and repeated activity sequences.

\- Use the results to guide further process-mining analysis.



