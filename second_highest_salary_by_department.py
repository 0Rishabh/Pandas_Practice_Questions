

# =========================================
# Question:
# Find the 2nd highest salary employee
# from each department
#
# Final output:
# department
# emp_id
# salary
# =========================================



# Import libraries
import pandas as pd



# Create DataFrame
employees = pd.DataFrame({
    "emp_id": [1,2,3,4,5,6,7,8],
    "department": ["IT","IT","HR","HR","Sales","Sales","IT","HR"],
    "salary": [70000,90000,50000,52000,60000,65000,85000,51000]
})



# Solution (same as provided)
result = (
    employees.assign(
        rank=employees.groupby('department')['salary']
                      .rank(method='dense', ascending=False)
    )
    .query('rank == 2')
    [['department', 'emp_id', 'salary']]
)

print(result)
