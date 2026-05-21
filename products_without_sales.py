


# =========================================
# Question:
# 👉 Products which never appeared
# in sales table.
#
# Final output:
# product_id
# product_name
# =========================================

# Import libraries
import pandas as pd

# Create DataFrames
products = pd.DataFrame({
    "product_id": [1,2,3,4],
    "product_name": ["Laptop","Mobile","Tablet","Mouse"]
})

sales = pd.DataFrame({
    "sale_id": [101,102,103,104],
    "product_id": [1,2,1,5],
    "quantity": [5,10,3,8]
})


# Solution 
df1 = products.merge(
    sales,
    on='product_id',
    how='left'
)

result = df1[
    df1['sale_id'].isna()
][['product_id','product_name']]

print(result)
