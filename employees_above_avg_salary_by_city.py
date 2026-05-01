

# =========================================
# Question:
# Find the number of employees in each city
# whose salary is greater than the
# overall average salary.
#
# Final output:
# city
# total_emp
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
data = {
    "emp_id": [101,102,103,104,105,106,107,108],
    "emp_name": ["Amit","Riya","Rahul","Neha","Arjun","Priya","Karan","Meera"],
    "city": ["Delhi","Mumbai","Bangalore","Delhi","Mumbai","Delhi","Mumbai","Bangalore"],
    "salary": [50000,45000,60000,40000,38000,47000,52000,41000]
}

df = pd.DataFrame(data)

# Solution (same as provided)
result = df[df['salary'] > df['salary'].mean()] \
    .groupby('city')['emp_id'] \
    .count() \
    .reset_index(name='total_emp')

print(result)
