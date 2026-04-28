# =========================================
# Problem: Find customers who have
# more than 2 orders AND total
# sales greater than 50000
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "order_id": [101,102,103,104,105,106,107,108,109,110],
    "customer": ["Amit","Riya","Amit","Rohan","Riya","Amit","Rohan","Riya","Amit","Rohan"],
    "city": ["Delhi","Mumbai","Delhi","Delhi","Mumbai","Delhi","Delhi","Mumbai","Delhi","Delhi"],
    "product": ["Laptop","Mobile","Mouse","Laptop","Mouse","Keyboard","Mouse","Laptop","Keyboard","Mobile"],
    "amount": [55000,20000,500,60000,700,1500,400,65000,2000,18000],
    "order_date": pd.to_datetime([
        "2024-01-05","2024-01-07","2024-01-10","2024-01-15","2024-01-18",
        "2024-01-20","2024-01-22","2024-01-25","2024-01-28","2024-01-30"
    ])
})

# Solution: Using groupby + agg + filter
result = df.groupby("customer").agg(
    total_sales=("amount", "sum"),
    num_orders=("order_id", "size")
).reset_index()

# Apply conditions
result = result[
    (result["num_orders"] > 2) &
    (result["total_sales"] > 50000)
]

# Final sorting
result = result.sort_values(
    by="total_sales",
    ascending=False
)

print(result)
