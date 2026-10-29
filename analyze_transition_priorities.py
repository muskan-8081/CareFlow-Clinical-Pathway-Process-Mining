
import pandas as pd
from pathlib import Path

input_file = Path("data/activity_pair_analysis.csv")
output_file = Path("data/transition_priority_analysis.csv")

if not input_file.exists():
    raise FileNotFoundError(
        f"{input_file} not found. Run analyze_activity_pairs.py first."
    )

df = pd.read_csv(input_file)

# Keep pairs with at least 10 recorded transitions
df = df[df["Transition_Count"] >= 10].copy()

# Flag return-visit transitions for separate interpretation
df["Transition_Type"] = "Within-pathway candidate"
df.loc[
    df["Current Activity"].eq("Return ER"),
    "Transition_Type"
] = "Potential return visit"

# Rank by frequency of intervals exceeding 6 hours,
# then by median elapsed time, then transition count.
df = df.sort_values(
    ["Over_360_Minutes", "Median_Minutes", "Transition_Count"],
    ascending=[False, False, False]
)

df.insert(0, "Priority_Rank", range(1, len(df) + 1))
df.to_csv(output_file, index=False)

print("Transition priority analysis completed!")
print("Activity pairs assessed:", len(df))
print("Saved to:", output_file)

print("\nTop 15 transitions with the most intervals over 6 hours:")
print(
    df.sort_values(
        ["Over_360_Minutes", "Transition_Count"],
        ascending=[False, False]
    )[
        [
            "Previous Activity",
            "Current Activity",
            "Transition_Count",
            "Median_Minutes",
            "Over_360_Minutes",
            "Transition_Type"
        ]
    ].head(15).to_string(index=False)
)

print("\nPotential within-pathway candidates:")
within_pathway = df[
    df["Transition_Type"] == "Within-pathway candidate"
]

print(
    within_pathway[
        [
            "Previous Activity",
            "Current Activity",
            "Transition_Count",
            "Median_Minutes",
            "Over_360_Minutes"
        ]
    ].head(15).to_string(index=False)
)

print(
    "\nNote: These are investigation priorities, "
    "not confirmed clinical bottlenecks."
)
