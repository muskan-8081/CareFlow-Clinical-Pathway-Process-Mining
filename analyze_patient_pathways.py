
import pandas as pd

# Load dataset
df = pd.read_csv("data/events.csv")

# Convert timestamps
df["time:timestamp"] = pd.to_datetime(
    df["time:timestamp"], errors="coerce"
)

# Remove records missing essential fields
df = df.dropna(
    subset=["case:concept:name", "concept:name", "time:timestamp"]
)

# Sort patient activities chronologically
df = df.sort_values(
    ["case:concept:name", "time:timestamp"]
)

# Create patient activity sequences
pathways = (
    df.groupby("case:concept:name")["concept:name"]
    .agg(list)
    .reset_index()
)

pathways["Activity_Count"] = pathways["concept:name"].apply(len)

pathways["Patient_Pathway"] = pathways["concept:name"].apply(
    lambda activities: " -> ".join(activities)
)

# Save individual patient pathways
pathways[
    ["case:concept:name", "Activity_Count", "Patient_Pathway"]
].rename(
    columns={"case:concept:name": "Case_ID"}
).to_csv(
    "data/patient_pathway_sequences.csv",
    index=False
)

# Identify most common complete activity sequences
pathway_summary = (
    pathways.groupby("Patient_Pathway")
    .agg(
        Number_of_Cases=("case:concept:name", "count"),
        Average_Activities=("Activity_Count", "mean")
    )
    .reset_index()
    .sort_values("Number_of_Cases", ascending=False)
)

pathway_summary.to_csv(
    "data/common_patient_pathways.csv",
    index=False
)

# Summarize pathway lengths
length_summary = (
    pathways.groupby("Activity_Count")
    .agg(Number_of_Cases=("case:concept:name", "count"))
    .reset_index()
    .sort_values("Activity_Count")
)

length_summary.to_csv(
    "data/patient_pathway_length_summary.csv",
    index=False
)

# Display results
print("\nPATIENT PATHWAY ANALYSIS COMPLETED")
print("----------------------------------")

print("Total patient cases:", len(pathways))
print("Unique pathway patterns:", len(pathway_summary))

print("\nTOP 10 COMMON PATIENT PATHWAYS")
print(pathway_summary.head(10).to_string(index=False))

print("\nPATHWAY LENGTH SUMMARY")
print(length_summary.to_string(index=False))

print("\nGenerated files:")
print("data/patient_pathway_sequences.csv")
print("data/common_patient_pathways.csv")
print("data/patient_pathway_length_summary.csv")
