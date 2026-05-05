

# =========================================
# Question:
# Calculate 3-day rolling average of sales
# Return only those days where:
# - rolling average is greater than 300
#
# Final output:
# date
# sales
# rolling_avg
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "date": pd.to_datetime([
        "2024-01-01","2024-01-02","2024-01-03","2024-01-04","2024-01-05",
        "2024-01-06","2024-01-07","2024-01-08","2024-01-09","2024-01-10"
    ]),
    "sales": [100,200,150,300,250,400,350,500,450,550]
})

# Solution 
df['rolling_avg'] = df['sales'].rolling(window=3).mean()

result = df[['date','sales','rolling_avg']] \
    .sort_values(by='date') \
    .query('rolling_avg > 300')

print(result)
