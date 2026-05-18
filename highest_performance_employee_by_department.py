

# =========================================
# Question:
# For each department:
#
# 👉 find employee having highest performance_score
#
# Expected output should contain:
#
# department
# emp_id
# performance_score
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
data = {
    "emp_id": [101,102,103,104,105,106,107],
    "department": ["IT","HR","IT","Sales","Sales","HR","IT"],
    "performance_score": [88,75,92,80,95,78,85]
}

df = pd.DataFrame(data)


# Solution
df['rnk'] = df.groupby('department')['performance_score'] \
              .rank(method='min', ascending=False)

result = df[df['rnk'] == 1]

print(result)
