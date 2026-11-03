import pandas as pd

# Load dataset
df = pd.read_csv("data/events.csv")

# Convert timestamps
df["time:timestamp"] = pd.to_datetime(
    df["time:timestamp"], errors="coerce"
)

# Remove records with missing essential values
df = df.dropna(
    subset=["case:concept:name", "concept:name", "time:timestamp"]
)

# Sort activities chronologically
df = df.sort_values(
    ["case:concept:name", "time:timestamp"]
)

# Create patient activity sequences
pathways = (
    df.groupby("case:concept:name")["concept:name"]
    .agg(list)
)

# Analyze first 3, 5 and 8 activities
results = []

for prefix_length in [3, 5, 8]:

    prefixes = pathways.apply(
        lambda activities: " -> ".join(
            activities[:prefix_length]
        )
    )

    summary = (
        prefixes.value_counts()
        .reset_index()
    )

    summary.columns = [
        "Activity_Prefix",
        "Number_of_Cases"
    ]

    summary["Prefix_Length"] = prefix_length

    results.append(summary)

# Combine results
final_summary = pd.concat(
    results, ignore_index=True
)

final_summary = final_summary[
    ["Prefix_Length", "Activity_Prefix", "Number_of_Cases"]
]

# Save results
final_summary.to_csv(
    "data/patient_pathway_prefix_analysis.csv",
    index=False
)

# Display results
print("\nPATIENT PATHWAY PREFIX ANALYSIS COMPLETED")
print("-----------------------------------------")

for length in [3, 5, 8]:

    print(f"\nTOP 10 COMMON {length}-ACTIVITY PREFIXES")

    print(
        final_summary[
            final_summary["Prefix_Length"] == length
        ]
        .head(10)
        .to_string(index=False)
    )

print("\nTotal patient cases analyzed:", len(pathways))

print("\nGenerated file:")
print("data/patient_pathway_prefix_analysis.csv")