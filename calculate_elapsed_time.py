
import pandas as pd
from pathlib import Path

# File paths
input_file = Path("data/events.csv")
output_file = Path("data/elapsed_time_analysis.csv")

# Load dataset
df = pd.read_csv(input_file)

# Convert timestamps into datetime format
df["time:timestamp"] = pd.to_datetime(
    df["time:timestamp"], errors="coerce", utc=True
)

# Remove rows missing Case ID or timestamp
df = df.dropna(
    subset=["case:concept:name", "time:timestamp"]
).copy()

# Sort events chronologically within each case
df = df.sort_values(
    ["case:concept:name", "time:timestamp"]
).copy()

# Get previous activity and timestamp for each case
grouped = df.groupby("case:concept:name", sort=False)

df["Previous Activity"] = grouped["concept:name"].shift(1)
df["Previous Timestamp"] = grouped["time:timestamp"].shift(1)

# Calculate elapsed time in minutes
df["Elapsed Time (Minutes)"] = (
    df["time:timestamp"] - df["Previous Timestamp"]
).dt.total_seconds() / 60

# Keep only rows with a previous event in the same case
result = df.dropna(
    subset=["Previous Activity", "Previous Timestamp"]
).copy()

# Rename columns for the output
result = result.rename(columns={
    "case:concept:name": "Case ID",
    "concept:name": "Current Activity",
    "time:timestamp": "Current Timestamp"
})

# Select required columns
result = result[[
    "Case ID",
    "Previous Activity",
    "Current Activity",
    "Previous Timestamp",
    "Current Timestamp",
    "Elapsed Time (Minutes)"
]]

# Save results
result.to_csv(output_file, index=False)

print("Elapsed time analysis completed!")
print("Total transitions:", len(result))
print("Unique cases:", result["Case ID"].nunique())
print("Saved to:", output_file)

print("\nSample results:")
print(result.head(10).to_string(index=False))

# Summary statistics
print("\nElapsed Time Summary (minutes):")
print(result["Elapsed Time (Minutes)"].describe())
# Investigate the 20 longest elapsed-time intervals
print("\nTop 20 longest elapsed-time intervals:")

top_intervals = result.sort_values(
    "Elapsed Time (Minutes)", ascending=False
).head(20)

print(top_intervals.to_string(index=False))

# Count intervals exceeding selected thresholds
print("\nIntervals exceeding thresholds:")

for threshold in [60, 360, 1440]:
    count = (
        result["Elapsed Time (Minutes)"] > threshold
    ).sum()
    print(f"More than {threshold} minutes: {count}")

# Count zero-minute intervals
zero_count = (
    result["Elapsed Time (Minutes)"] == 0
).sum()

print("Zero-minute intervals:", zero_count)
# Investigate the 20 longest elapsed-time intervals
print("\nTop 20 longest elapsed-time intervals:")

top_intervals = result.sort_values(
    "Elapsed Time (Minutes)", ascending=False
).head(20)

print(top_intervals.to_string(index=False))

# Count intervals exceeding selected thresholds
print("\nIntervals exceeding thresholds:")

for threshold in [60, 360, 1440]:
    count = (result["Elapsed Time (Minutes)"] > threshold).sum()
    print(f"More than {threshold} minutes: {count}")

# Count zero-minute intervals
zero_count = (result["Elapsed Time (Minutes)"] == 0).sum()
print("Zero-minute intervals:", zero_count)
print(result["Elapsed Time (Minutes)"].describe())

# Investigate the 20 longest elapsed-time intervals
print("\nTop 20 longest elapsed-time intervals:")

top_intervals = result.sort_values(
    "Elapsed Time (Minutes)", ascending=False
).head(20)

print(top_intervals.to_string(index=False))

# Count intervals exceeding selected thresholds
print("\nIntervals exceeding thresholds:")

for threshold in [60, 360, 1440]:
    count = (result["Elapsed Time (Minutes)"] > threshold).sum()
    print(f"More than {threshold} minutes: {count}")

# Count zero-minute intervals
zero_count = (result["Elapsed Time (Minutes)"] == 0).sum()
print("Zero-minute intervals:", zero_count)

