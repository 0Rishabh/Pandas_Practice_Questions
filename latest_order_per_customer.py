

# =========================================
# Question:
# For each customer:
#
# 👉 find their latest order
#
# Final output:
# order_id
# customer_id
# order_date
# =========================================


# Import libraries
import pandas as pd


# Create DataFrame
data = {
    "order_id": [1,2,3,4,5,6],
    "customer_id": [101,101,102,103,101,102],
    "order_date": [
        "2026-01-01",
        "2026-01-05",
        "2026-01-02",
        "2026-01-10",
        "2026-01-12",
        "2026-01-15"
    ]
}



df = pd.DataFrame(data)

df['order_date'] = pd.to_datetime(df['order_date'])


# Solution 
result = df.sort_values(by='order_date') \
           .groupby('customer_id') \
           .tail(1)

print(result)
