

# =========================================
# Question:
# For each department:
# - Rank employees based on salary (highest = rank 1)
# - Return only top 2 highest paid employees per department
#
# Final output:
# department
# employee
# salary
# rank
#
# Sort by:
# department
# rank
# =========================================


# Import libraries
import pandas as pd


# Create DataFrame
df = pd.DataFrame({
    "employee": ["Amit","Riya","John","Sara","Karan","Neha","Raj","Pooja","Vikas","Ankit"],
    "department": ["IT","IT","IT","HR","HR","HR","Sales","Sales","Sales","Sales"],
    "salary": [70000,80000,75000,50000,52000,51000,60000,58000,62000,61000]
})



# Solution 
df['rank'] = df.groupby('department')['salary'] \
               .rank(method='dense', ascending=False)

df = df[df['rank'] <= 2]

result = df.sort_values(by=['department', 'rank'])

print(result)
