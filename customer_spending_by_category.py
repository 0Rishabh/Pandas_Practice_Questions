

# =========================================
# Question:
# Find customers who spent:
#
# - more than 5000 in Electronics
# - and more than 2000 in Clothing
#
# Final output:
# customer
# electronics_spent
# clothing_spent
# =========================================


# Import libraries
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "customer": ["A","A","B","B","C","C","D","D","E","E"],
    "category": ["Electronics","Clothing","Electronics","Clothing",
                 "Electronics","Clothing","Electronics","Clothing",
                 "Electronics","Clothing"],
    "amount": [5000,2000,7000,1000,3000,4000,8000,1500,2000,2500]
})


# Solution 
temp = df.groupby(
    ['customer', 'category']
)['amount'] \
         .sum() \
         .unstack(fill_value=0)

result = temp[
    (temp['Electronics'] > 5000) &
    (temp['Clothing'] > 2000)
].reset_index()

print(result)
