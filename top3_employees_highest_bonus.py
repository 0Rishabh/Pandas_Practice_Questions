

# =========================================
# Problem: Find Top 3 employees
# with highest bonus amount
# =========================================

# Import libraries
import pandas as pd
import numpy as np

# Create main DataFrame
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

# Create bonus DataFrame
bonus_data = {
    "department": ["IT", "HR", "Sales"],
    "bonus_percent": [10, 8, 12]
}

bonus_df = pd.DataFrame(bonus_data)

# Merge employee data with bonus data
merged_df = pd.merge(
    df,
    bonus_df,
    on="department",
    how="left"
)

# Calculate bonus amount
merged_df["bonus_amount"] = (
    merged_df["salary"] * merged_df["bonus_percent"] / 100
)

# Get Top 3 employees with highest bonus
result = merged_df.sort_values(
    by="bonus_amount",
    ascending=False
).head(3)

print(result)
