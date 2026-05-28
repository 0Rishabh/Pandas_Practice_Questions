


# =========================================
# Question:
# Create a new column:
#
# 👉 expense_percent
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
data = {
    "department": ["IT","HR","Sales","Finance"],
    "expense": [50000,20000,30000,40000]
}

df = pd.DataFrame(data)


# Solution 
df['expense_percent'] = (
    df['expense'] / df['expense'].sum()
) * 100

print(df)
