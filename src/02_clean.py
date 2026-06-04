import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/sensor_data.csv")

# Null counts before cleaning
null_before = df.isnull().sum()

# Fill missing values in sensor columns
df["temp"] = df["temp"].fillna(df["temp"].median())
df["humidity"] = df["humidity"].fillna(df["humidity"].median())
df["co2"] = df["co2"].fillna(df["co2"].median())

# Remove rows with missing yield
df = df.dropna(subset=["yield"])

# Null counts after cleaning
null_after = df.isnull().sum()

# Save cleaned dataset
df.to_parquet(
    "data/processed/02_cleaned.parquet",
    index=False
)

# Create cleaning log
with open(
    "data/processed/cleaning_log.md",
    "w",
    encoding="utf-8"
) as f:

    f.write("# Cleaning Log\n\n")

    f.write("## Null Counts Before\n\n")
    f.write(null_before.to_string())

    f.write("\n\n## Null Counts After\n\n")
    f.write(null_after.to_string())

    f.write("\n\n## Imputation Rationale\n\n")
    f.write("- Temperature: Missing values replaced with median.\n")
    f.write("- Humidity: Missing values replaced with median.\n")
    f.write("- CO2: Missing values replaced with median.\n")
    f.write("- Yield: Rows with missing yield removed.\n")

print("Cleaning Complete")