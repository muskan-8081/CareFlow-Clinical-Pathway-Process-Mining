import pandas as pd

# Load original event dataset
df = pd.read_csv("data/events.csv")

# Convert timestamp column
df["time:timestamp"] = pd.to_datetime(
    df["time:timestamp"], errors="coerce"
)

# Cases selected from previous delay analysis
top_cases = ["HG", "VAA", "ZS", "LS", "UBA"]

results = []

for case_id in top_cases:
    case_data = df[
        df["case:concept:name"] == case_id
    ].sort_values("time:timestamp")

    print(f"\n{'=' * 50}")
    print(f"CASE ID: {case_id}")
    print(f"{'=' * 50}")

    for _, row in case_data.iterrows():
        print(
            row["concept:name"],
            "|",
            row["time:timestamp"]
        )

        results.append({
            "Case ID": case_id,
            "Activity": row["concept:name"],
            "Timestamp": row["time:timestamp"]
        })

# Save inspection results
output = pd.DataFrame(results)
output.to_csv(
    "data/long_interval_case_review.csv",
    index=False
)

print("\nCase inspection completed!")
print("Total cases inspected:", len(top_cases))
print("Output: data/long_interval_case_review.csv")