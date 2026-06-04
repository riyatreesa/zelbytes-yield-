import pandas as pd

df = pd.read_parquet("data/processed/02_cleaned.parquet")

df.head(50).to_csv(
    "data/processed/sample_50_rows.csv",
    index=False
)

print("Sample file created")