


# =========================================
# Question:
# For each department:
#
# find employee having maximum salary
#
# Final output:
# department
# employee
# salary
# =========================================




# Import libraries
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "employee": ["A","B","C","D","E","F","G","H"],
    "department": ["IT","IT","IT","HR","HR","Sales","Sales","Sales"],
    "salary": [70000,80000,75000,50000,52000,60000,65000,62000]
})



# Solution 
result = df.loc[
    df.groupby('department')['salary'].idxmax(),
    ['department', 'employee', 'salary']
]

print(result)
