

# =========================================
# Question:
# For each customer:
# - Calculate running total of amount based on date
# - Return rows where running total is greater than 4000
#
# Final output:
# customer
# date
# amount
# running_total
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "customer": ["A","A","A","B","B","B","C","C","C","C"],
    "date": pd.to_datetime([
        "2024-01-01","2024-01-05","2024-01-10",
        "2024-01-02","2024-01-06","2024-01-12",
        "2024-01-03","2024-01-07","2024-01-11","2024-01-15"
    ]),
    "amount": [1000,2000,1500,3000,2500,4000,500,700,900,1200]
})

# Solution 1 (method chaining)
result = df.sort_values(['customer','date']) \
    .assign(running_total=lambda x: x.groupby('customer')['amount'].cumsum()) \
    .query('running_total > 4000') \
    [['customer','date','amount','running_total']]

print(result)

# Solution 2 (step-by-step)
df = df.sort_values(by=['customer','date'])
df['running_total'] = df.groupby('customer')['amount'].cumsum()

result2 = df[df['running_total'] > 4000][
    ['customer','date','amount','running_total']
]

print(result2)
