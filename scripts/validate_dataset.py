
import pandas as pd
from pathlib import Path

data_path = Path("data/events.csv")
df = pd.read_csv(data_path)

case_col = "case:concept:name"
activity_col = "concept:name"
timestamp_col = "time:timestamp"

df[timestamp_col] = pd.to_datetime(
    df[timestamp_col], errors="coerce", utc=True
)

print("=== CAREFLOW DATA QUALITY REPORT ===")
print("Total events:", len(df))
print("Total columns:", len(df.columns))
print("Unique cases:", df[case_col].nunique())
print("Missing case IDs:", df[case_col].isna().sum())
print("Missing activity names:", df[activity_col].isna().sum())
print("Invalid timestamps:", df[timestamp_col].isna().sum())

print("\nTop activities:")
print(df[activity_col].value_counts().head(15))

print("\nLifecycle transitions:")
print(df["lifecycle:transition"].value_counts(dropna=False))

print("\nDuplicate case/activity/timestamp rows:")
print(
    df.duplicated(
        subset=[case_col, activity_col, timestamp_col]
    ).sum()
)

print("\nEarliest event:", df[timestamp_col].min())
print("Latest event:", df[timestamp_col].max())

print("\n=== VALIDATION COMPLETE ===")
