

# =========================================
# Question:
# Create a new column:
# 👉 previous_month_sales
#
# For each product, show previous month's sales
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
data = {
    "product": ["Laptop","Laptop","Laptop","Mobile","Mobile","Mobile"],
    "month": ["Jan","Feb","Mar","Jan","Feb","Mar"],
    "sales": [500,700,650,300,450,400]
}

df = pd.DataFrame(data)





# Solution 
df['pre_month_sales'] = df['sales'].shift(1)

print(df)
