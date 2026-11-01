
import pandas as pd

# Load original event dataset
df = pd.read_csv("data/events.csv")

# Convert timestamps
df["time:timestamp"] = pd.to_datetime(
    df["time:timestamp"], errors="coerce"
)

# Remove rows missing essential fields
df = df.dropna(
    subset=["case:concept:name", "concept:name"]
)

# Analyze activity repetition within each case
repeated = (
    df.groupby(
        ["case:concept:name", "concept:name"]
    )
    .agg(
        Activity_Count=("concept:name", "size"),
        First_Recorded=("time:timestamp", "min"),
        Last_Recorded=("time:timestamp", "max")
    )
    .reset_index()
)

# Keep activities occurring more than once per case
repeated = repeated[
    repeated["Activity_Count"] > 1
].copy()

# Rename columns
repeated.rename(
    columns={
        "case:concept:name": "Case ID",
        "concept:name": "Activity"
    },
    inplace=True
)

# Sort by repetition count
repeated = repeated.sort_values(
    by="Activity_Count",
    ascending=False
)

# Save detailed results
repeated.to_csv(
    "data/repeated_activity_analysis.csv",
    index=False
)

# Activity-level summary
summary = (
    repeated.groupby("Activity")
    .agg(
        Cases_With_Repetition=("Case ID", "nunique"),
        Total_Repeated_Events=("Activity_Count", "sum"),
        Maximum_Repetitions=("Activity_Count", "max")
    )
    .reset_index()
    .sort_values(
        by="Cases_With_Repetition",
        ascending=False
    )
)

summary.to_csv(
    "data/repeated_activity_summary.csv",
    index=False
)

# Display results
print("\nREPEATED ACTIVITY ANALYSIS COMPLETED")
print("------------------------------------")
print("Total event records:", len(df))
print("Cases with repeated activities:",
      repeated["Case ID"].nunique())
print("Repeated case-activity combinations:", len(repeated))

print("\nTOP 15 REPEATED ACTIVITIES")
print(summary.head(15).to_string(index=False))

print("\nGenerated files:")
print("data/repeated_activity_analysis.csv")
print("data/repeated_activity_summary.csv")
