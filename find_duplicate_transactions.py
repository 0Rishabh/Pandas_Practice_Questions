


# =========================================
# Question:
# Find duplicate transactions based on:
# - same customer_id
# - same amount
#
# Return all duplicate rows.
#
# Final output:
# transaction_id
# customer_id
# amount
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "transaction_id": [101,102,103,104,105,106,107,108,109,110],
    "customer_id": [1,2,1,3,2,1,3,2,1,3],
    "amount": [500,700,500,900,700,1200,900,700,500,1000]
})



# Solution
result = df[df.duplicated(
    ['customer_id', 'amount'],
    keep=False
)]

print(result)
