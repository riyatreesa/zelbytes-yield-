# Cleaning Log

## Null Counts Before

temp        6
humidity    6
co2         6
yield       3

## Null Counts After

temp        0
humidity    0
co2         0
yield       0

## Imputation Rationale

- Temperature: Missing values replaced with median.
- Humidity: Missing values replaced with median.
- CO2: Missing values replaced with median.
- Yield: Rows with missing yield removed.
