

# =========================================
# Pandas Interview Question
# Question:
# For each customer:
# - Calculate days difference between current order and previous order
#   (Hint: use diff() on date after sorting)
#
# Then return only those rows where:
# - difference between orders is greater than 3 days
#
# Final output:
# customer_name
# order_id
# order_date
# days_diff
#
# Sort by:
# customer_name
# order_date
# =========================================

# Import libraries
import pandas as pd

# Create DataFrames
orders = pd.DataFrame({
    "order_id": [1,2,3,4,5,6,7,8,9,10],
    "customer_id": [101,101,102,102,103,101,103,102,101,103],
    "order_date": pd.to_datetime([
        "2024-01-01","2024-01-05","2024-01-02","2024-01-06","2024-01-03",
        "2024-01-10","2024-01-08","2024-01-12","2024-01-15","2024-01-18"
    ]),
    "amount": [500,700,300,400,800,600,900,200,1000,1200]
})

customers = pd.DataFrame({
    "customer_id": [101,102,103],
    "customer_name": ["Amit","Riya","Rohan"]
})


# Solution
merged = orders.merge(customers, on='customer_id')

merged = merged.sort_values(by=['customer_id', 'order_date'])

merged['days_diff'] = merged.groupby('customer_id')['order_date'].diff().dt.days

result = merged[merged['days_diff'] > 3]

result = result.sort_values(by=['customer_name', 'order_date'])[
    ['customer_name', 'order_id', 'order_date', 'days_diff']
]

print(result)
