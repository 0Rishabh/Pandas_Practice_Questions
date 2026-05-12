

# =========================================
# Question:
# For each customer:
#       Growth% 
# - calculate previous order amount using shift()
# - find percentage growth from previous order
#
# Final output:
# customer_id
# order_date
# amount
# prev_amount
# growth_percent
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "customer_id": [1,1,1,2,2,3,3,3,3],
    "order_date": pd.to_datetime([
        "2024-01-01","2024-01-05","2024-01-10",
        "2024-01-02","2024-01-08",
        "2024-01-01","2024-01-03","2024-01-06","2024-01-12"
    ]),
    "amount": [500,700,600,1000,1200,300,400,500,800]
})

# Solution (same as provided)
df = df.sort_values(by=['customer_id', 'order_date'])

df['prev_amount'] = df.groupby('customer_id')['amount'].shift(1)

df['growth_percent'] = (
    (df['amount'] - df['prev_amount']) / df['prev_amount']
) * 100

result = df[[
    'customer_id',
    'order_date',
    'amount',
    'prev_amount',
    'growth_percent'
]]

print(result)
