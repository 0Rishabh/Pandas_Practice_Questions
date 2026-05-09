

# =========================================
# Question:
# Find employees whose salary is greater
# than department average salary
#
# Final output:
# emp_id
# department
# salary
# dept_avg_salary
#
# Sort by department.
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "emp_id": [1,2,3,4,5,6,7,8,9,10],
    "department": ["IT","IT","HR","HR","Sales","Sales","IT","HR","Sales","IT"],
    "salary": [70000,80000,50000,52000,60000,62000,75000,51000,61000,90000]
})

# Solution 
df['dept_avg_salary'] = df.groupby('department')['salary'].transform('mean')

result = df[df['salary'] > df['dept_avg_salary']] \
    .sort_values(by='department')[
        ['emp_id', 'department', 'salary', 'dept_avg_salary']
    ]

print(result)
