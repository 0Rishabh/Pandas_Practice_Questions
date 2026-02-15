



# =========================================
# Problem: Find the number of
# missing (NULL) values in each column
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
    "salary": [50000,45000,60000,40000,38000,50000,52000,41000],
    "sales": [200,150,300,250,180,np.nan,220,np.nan],
    "month": ["Jan","Jan","Feb","Feb","Jan","Feb","Jan","Feb"],
    "experience_years": [2,3,4,1,2,3,2,np.nan]
}

df = pd.DataFrame(data)

# Solution: Count missing values column-wise
result = df.isnull().sum()
print(result)
