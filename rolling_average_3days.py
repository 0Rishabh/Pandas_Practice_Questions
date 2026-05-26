\


# =========================================
# Question:
# Create a new column:
#
# 👉 rolling_avg_3days
#
# It should contain:
# - average of current row
# - and previous 2 rows
# =========================================



# Import libraries
import pandas as pd
\

# Create DataFrame
data = {
    "date": [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03",
        "2026-01-04",
        "2026-01-05"
    ],
    "sales": [100,150,200,250,300]
}

df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'])


# Solution 
df['rolling_avg_3days'] = df['sales'].rolling(
    window=3
).mean()

print(df)
