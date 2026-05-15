


# =========================================
# Question:
# For each store:
# - calculate month-over-month sales difference using diff()
# - find stores where sales decreased compared to previous month
#
# Final output:
# store
# month
# sales
# sales_diff
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "store": ["A","A","A","B","B","B","C","C","C"],
    "month": ["Jan","Feb","Mar","Jan","Feb","Mar","Jan","Feb","Mar"],
    "sales": [1000,1200,900,2000,2500,2400,1500,1800,2200]
})



# Solution 

df = df.sort_values(by=['store', 'month'])

df['sales_diff'] = df.groupby('store')['sales'].diff()

result = df[df['sales_diff'] < 0][
    ['store', 'month', 'sales', 'sales_diff']
]

print(result)
