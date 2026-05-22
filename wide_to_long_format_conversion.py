


# =========================================
# Question:
# Convert this wide-format data
# into long-format using Pandas.
#
# Expected columns:
# month
# product
# sales
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "month": ["Jan","Feb","Mar"],
    "Laptop": [50000,52000,51000],
    "Mouse": [2000,2200,2100],
    "Keyboard": [3000,3200,3100]
})


# Solution 
result = df.melt(
    id_vars='month',
    var_name='product',
    value_name='sales'
)

print(result)
