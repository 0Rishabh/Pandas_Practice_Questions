

# =========================================
# Question:
# Find total amount spent by each customer_name,
# but only include:
# - customers from Delhi
# - whose total spending is greater than 10,000
#
# Final output:
#     customer_name
#     total_spent
#
# Sort by total_spent descending.
# =========================================

# Import libraries
import pandas as pd

# Create DataFrames
orders = pd.DataFrame({
    "order_id": [101,102,103,104,105,106,107,108],
    "customer_id": [1,2,1,3,2,1,3,2],
    "amount": [5000,7000,3000,4000,6500,3000,4500,8000]
})

customers = pd.DataFrame({
    "customer_id": [1,2,3],
    "customer_name": ["Amit","Riya","Rohan"],
    "city": ["Delhi","Mumbai","Delhi"]
})

# Solution
merge_data = orders.merge(customers, on='customer_id', how='inner')

merge_data = merge_data[merge_data['city'] == 'Delhi']

result = merge_data.groupby('customer_name').agg(
    total_amount=('amount', 'sum')
).reset_index().sort_values(
    by='total_amount',
    ascending=False
)

result = result[result['total_amount'] > 10000]

print(result)
