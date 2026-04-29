


# =========================================
# Find the average salary of each department,
# but only for employees:
# - whose salary is greater than 50,000
# - and experience is at least 4 years
#     Final output:
#         department
#         avg_salary
#
# Sort by avg_salary descending.
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "emp_id": [1,2,3,4,5,6,7,8,9,10],
    "department": ["HR","IT","IT","Sales","HR","IT","Sales","HR","IT","Sales"],
    "employee": ["Amit","Riya","John","Sara","Karan","Neha","Raj","Pooja","Vikas","Ankit"],
    "salary": [40000,70000,65000,50000,42000,80000,55000,45000,72000,58000],
    "experience": [2,5,4,3,1,6,4,2,5,3]
})

# Solution (same as provided)
df = df[(df['salary'] > 50000) & (df['experience'] >= 4)]

grouped_df = df.groupby('department').agg(
    avg_salary=('salary', 'mean')
).reset_index().sort_values(
    by='avg_salary',
    ascending=False
)

print(grouped_df)
