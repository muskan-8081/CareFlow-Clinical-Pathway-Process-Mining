
import pandas as pd
from pathlib import Path

# File paths
input_file = Path("data/elapsed_time_analysis.csv")
output_file = Path("data/activity_pair_analysis.csv")

# Load elapsed-time analysis
df = pd.read_csv(input_file)

# Group consecutive activities into pairs
summary = (
    df.groupby(
        ["Previous Activity", "Current Activity"],
        dropna=False
    )
    .agg(
        Transition_Count=("Elapsed Time (Minutes)", "size"),
        Mean_Minutes=("Elapsed Time (Minutes)", "mean"),
        Median_Minutes=("Elapsed Time (Minutes)", "median"),
        Max_Minutes=("Elapsed Time (Minutes)", "max"),
        Over_60_Minutes=(
            "Elapsed Time (Minutes)",
            lambda x: (x > 60).sum()
        ),
        Over_360_Minutes=(
            "Elapsed Time (Minutes)",
            lambda x: (x > 360).sum()
        )
    )
    .reset_index()
)

# Sort by frequency
summary = summary.sort_values(
    "Transition_Count", ascending=False
)

# Save the complete activity-pair report
summary.to_csv(output_file, index=False)

print("Activity-pair analysis completed!")
print("Unique activity pairs:", len(summary))
print("Saved to:", output_file)

print("\nTop 15 activity pairs by frequency:")
print(
    summary.head(15).to_string(index=False)
)

print("\nTop 15 activity pairs by median elapsed time (minimum 10 transitions):")
frequent_pairs = summary[summary["Transition_Count"] >= 10]

print(
    frequent_pairs.sort_values(
        "Median_Minutes", ascending=False
    ).head(15).to_string(index=False)
)
