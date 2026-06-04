import pandas as pd
import numpy as np

np.random.seed(42)

rows = 200

df = pd.DataFrame({
"temp": np.random.normal(24, 2, rows),
"humidity": np.random.normal(85, 5, rows),
"co2": np.random.normal(900, 80, rows),
"yield": np.random.normal(1.5, 0.2, rows)
})

df.loc[5:10, "temp"] = np.nan
df.loc[20:25, "humidity"] = np.nan
df.loc[40:45, "co2"] = np.nan
df.loc[60:62, "yield"] = np.nan

df.to_csv("data/raw/sensor_data.csv", index=False)

print("Dataset created successfully")
