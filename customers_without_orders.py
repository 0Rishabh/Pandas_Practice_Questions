


# =========================================
# Question:
# Find customers who never placed any order.
#
# Final output:
# customer_id
# customer_name
# city
# =========================================



# Import libraries
import numpy as np
import pandas as pd


# Create DataFrames
customers = pd.DataFrame({
    "customer_id": [1,2,3,4],
    "customer_name": ["Amit","Riya","Karan","Neha"],
    "city": ["Delhi","Mumbai","Pune","Delhi"]
})

orders = pd.DataFrame({
    "order_id": [101,102,103,104],
    "customer_id": [1,2,1,5],
    "amount": [5000,7000,3000,4000]
})



# Solution 
df1 = customers.merge(
    orders,
    on="customer_id",
    how='left'
)

result = df1[
    df1['order_id'].isna()
][['customer_id','customer_name','city']]

print(result)
