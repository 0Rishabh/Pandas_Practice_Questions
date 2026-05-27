

# =========================================
# Question:
# Create a new column:
#
# 👉 cumulative_revenue
# =========================================



# Import libraries
import pandas as pd



# Create DataFrame
data = {
    "month": ["Jan","Feb","Mar","Apr","May"],
    "revenue": [1000,1500,1200,1800,2000]
}

df = pd.DataFrame(data)



# Solution 
df['cumulative_revenue'] = df['revenue'].cumsum()

print(df)
