import pandas as pd
import os

input_file = "data/events.parquet"
output_file = "data/events.csv"

df = pd.read_parquet(input_file)

# Ensure the data folder exists
os.makedirs("data", exist_ok=True)

# Save dataset as CSV
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("Conversion completed!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Column names:")
print(df.columns.tolist())
print("Saved to:", os.path.abspath(output_file))
print("File exists:", os.path.exists(output_file))