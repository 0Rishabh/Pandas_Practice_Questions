

# =========================================
# Problem: Show employees from
# Sales department AND salary > 39000
# =========================================

# Import libraries
import pandas as pd
import numpy as np

# Create DataFrame
data = {
    "emp_id": [101,102,103,104,105,106,107,108],
    "emp_name": ["Amit","Riya","Rahul","Neha","Arjun","Priya","Karan","Meera"],
    "department": ["IT","HR","IT","Sales","Sales","HR","IT","Sales"],
    "city": ["Delhi","Mumbai","Bangalore","Delhi","Mumbai","Delhi","Mumbai","Bangalore"],
    "salary": [50000,45000,60000,40000,38000,47000,52000,41000],
    "sales": [200,150,300,250,180,np.nan,220,270],
    "month": ["Jan","Jan","Feb","Feb","Jan","Feb","Jan","Feb"],
    "experience_years": [2,3,4,1,2,3,2,2]
}

df = pd.DataFrame(data)

# Solution: Sales department with salary > 39000
result = df[
    (df["department"] == "Sales") & 
    (df["salary"] > 39000)
]

print(result)
