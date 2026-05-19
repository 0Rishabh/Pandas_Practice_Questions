

# =========================================
# Question:
# Create a pivot table where:
#
# rows = region
# columns = product
# values = total sales
# =========================================



# Import libraries
import pandas as pd


# Create DataFrame
df = pd.DataFrame({
    "region": ["North","North","South","South","East","East","West","West"],
    "product": ["Laptop","Mouse","Laptop","Mouse","Laptop","Mouse","Laptop","Mouse"],
    "sales": [50000,2000,45000,1500,47000,1800,52000,2200]
})




# Solution 1 : groupby + unstack
result1 = df.groupby(
    ['region', 'product']
)['sales'] \
  .sum() \
  .unstack()

print(result1)



# Solution 2 : pivot_table
result2 = df.pivot_table(
    index='region',
    columns='product',
    values='sales',
    aggfunc='sum'
)

print(result2)
