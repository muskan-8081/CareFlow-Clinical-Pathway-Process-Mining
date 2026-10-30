
import pandas as pd
from pathlib import Path

# File paths
input_file = Path("data/elapsed_time_analysis.csv")
output_dir = Path("data")

# Load dataset
if not input_file.exists():
    raise FileNotFoundError("Elapsed time CSV file not found.")

df = pd.read_csv(input_file)

print("Dataset loaded successfully!")
print("Total records:", len(df))

# Clean column headings
df.columns = df.columns.str.strip()

# Convert elapsed time to numeric
df["Elapsed Time (Minutes)"] = pd.to_numeric(
    df["Elapsed Time (Minutes)"], errors="coerce"
)

df = df.dropna(subset=["Elapsed Time (Minutes)"]).copy()

# Calculate hours
df["Elapsed Hours"] = df["Elapsed Time (Minutes)"] / 60

# Select intervals exceeding 6 hours
long_intervals = df[
    df["Elapsed Time (Minutes)"] > 360
].copy()

# Classify transitions
def classify_transition(row):
    previous = str(row["Previous Activity"])
    current = str(row["Current Activity"])

    if previous.startswith("Release") and current == "Return ER":
        return "Potential return visit"

    elif previous == current:
        return "Repeated activity"

    elif previous == "Admission NC" and current in [
        "CRP", "Leucocytes"
    ]:
        return "Transition requiring investigation"

    else:
        return "Other transition"

long_intervals["Investigation Category"] = (
    long_intervals.apply(classify_transition, axis=1)
)

# Add observations
def create_observation(row):
    category = row["Investigation Category"]

    if category == "Potential return visit":
        return "Check whether this represents a separate ER visit."

    elif category == "Repeated activity":
        return "Investigate repeated activity and clinical context."

    elif category == "Transition requiring investigation":
        return "Examine the complete case timeline."

    return "Review the activity sequence and elapsed interval."

long_intervals["Observation"] = (
    long_intervals.apply(create_observation, axis=1)
)

# Sort longest intervals first
long_intervals = long_intervals.sort_values(
    "Elapsed Time (Minutes)", ascending=False
)

# Save detailed report
detail_file = output_dir / "case_level_delay_analysis.csv"
long_intervals.to_csv(detail_file, index=False)

# Case-level summary
case_summary = (
    long_intervals.groupby("Case ID")
    .agg(
        Long_Interval_Count=("Elapsed Time (Minutes)", "count"),
        Maximum_Interval_Minutes=("Elapsed Time (Minutes)", "max"),
        Median_Interval_Minutes=("Elapsed Time (Minutes)", "median"),
        Total_Long_Interval_Minutes=("Elapsed Time (Minutes)", "sum")
    )
    .reset_index()
)

case_summary["Maximum_Interval_Hours"] = (
    case_summary["Maximum_Interval_Minutes"] / 60
)

case_summary = case_summary.sort_values(
    "Maximum_Interval_Minutes", ascending=False
)

summary_file = output_dir / "case_level_delay_summary.csv"
case_summary.to_csv(summary_file, index=False)

# Category summary
category_summary = (
    long_intervals.groupby("Investigation Category")
    .agg(
        Transition_Count=("Elapsed Time (Minutes)", "count"),
        Average_Hours=("Elapsed Hours", "mean"),
        Median_Hours=("Elapsed Hours", "median"),
        Maximum_Hours=("Elapsed Hours", "max")
    )
    .reset_index()
)

category_file = output_dir / "case_level_category_summary.csv"
category_summary.to_csv(category_file, index=False)

# Display results
print("\nCASE-LEVEL INVESTIGATION COMPLETED")
print("----------------------------------")
print("Total transitions:", len(df))
print("Intervals above 6 hours:", len(long_intervals))
print("Unique cases investigated:",
      long_intervals["Case ID"].nunique())

print("\nDetailed report:", detail_file)
print("Case summary:", summary_file)
print("Category summary:", category_file)

print("\nTOP 10 CASES")
print(case_summary.head(10).to_string(index=False))

print("\nCATEGORY SUMMARY")
print(category_summary.to_string(index=False))
