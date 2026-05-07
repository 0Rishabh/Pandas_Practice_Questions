



# =========================================
# Question:
# Find most frequently purchased product for each customer
#
# Rules:
# - If tie happens → take product with higher total amount
#
# Final output:
# customer
# product
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "customer": ["A","A","A","B","B","C","C","C","C","D"],
    "product": ["Laptop","Mouse","Laptop","Laptop","Mouse","Mouse","Laptop","Mouse","Keyboard","Laptop"],
    "amount": [50000,500,52000,48000,700,400,51000,600,1500,47000]
})


# Solution
temp = df.groupby(['customer', 'product']).agg(
    total=('product', 'count'),
    total_amount=('amount', 'sum')
).reset_index()

temp = temp.sort_values(
    by=['customer', 'total', 'total_amount'],
    ascending=[True, False, False]
)

result = temp.groupby('customer').head(1)[
    ['customer', 'product']
]

print(result)
