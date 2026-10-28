# CareFlow: Elapsed Time Analysis

## Objective
Analyze the time between consecutive recorded clinical activities to identify long intervals and patterns in patient journeys.

## Dataset Summary
- Total recorded transitions: 14,141
- Unique patient cases: 1,049
- Mean elapsed time: 3,042.76 minutes
- Median elapsed time: 6.53 minutes
- 75th percentile: 435 minutes
- Maximum elapsed time: 600,855.3 minutes

## Interval Analysis
- Transitions exceeding 60 minutes: 5,159
- Transitions exceeding 360 minutes: 3,668
- Transitions exceeding 1,440 minutes: 2,122
- Transitions with zero elapsed minutes: 4,441

## Key Findings
1. The elapsed-time distribution is highly skewed: the mean is much larger than the median.
2. Many consecutive activities share the same timestamp.
3. Some of the longest intervals occur between `Release A` and `Return ER`, potentially representing a return visit after discharge.
4. Long intervals require activity-specific analysis before they can be classified as operational delays.

## Limitations
Elapsed time represents the difference between consecutive recorded event timestamps. It does not necessarily measure actual treatment duration or waiting time. Zero-minute intervals may indicate activities recorded at the same time.

## Next Steps
- Analyze transitions by activity pair.
- Separate return visits from within-visit transitions where the dataset supports it.
- Investigate long intervals within clinical pathways.
- Use the findings to guide further process-mining analysis.
