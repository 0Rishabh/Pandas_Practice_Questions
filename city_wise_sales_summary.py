


# =========================================
# Question:
# Find for each city:
# 👉 total amount
# 👉 average amount
# 👉 number of completed orders only
#
# Final output:
# city
# Total_amount
# Avg_amount
# Completed_orders
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
data = {
    "order_id": [1,2,3,4,5,6,7,8],
    "customer": ["A","B","A","C","B","D","A","C"],
    "city": ["Delhi","Mumbai","Delhi","Delhi","Mumbai","Pune","Delhi","Delhi"],
    "amount": [5000,7000,3000,4000,2000,6000,3500,4500],
    "status": ["Completed","Pending","Completed","Cancelled","Completed","Completed","Pending","Completed"]
}

df = pd.DataFrame(data)

# Solution 
result = df.groupby('city', as_index=False).agg(
    Total_amount=('amount', 'sum'),
    Avg_amount=('amount', 'mean'),
    Completed_orders=('status', lambda x: (x == 'Completed').sum())
)

print(result)
