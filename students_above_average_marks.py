

# =========================================
# Question:
# Find students whose average marks
# are greater than 70
#
# Final output:
# student
# avg_marks
# =========================================

# Import libraries
import pandas as pd

# Create DataFrame
data = {
    "student": ["A","A","B","B","C","C","D","D"],
    "subject": ["Math","English","Math","English","Math","English","Math","English"],
    "marks": [80,70,60,50,90,95,40,45]
}

df = pd.DataFrame(data)

# Solution 
result = df.groupby('student', as_index=False).agg(
    avg_marks=('marks', 'mean')
).query('avg_marks > 70')

print(result)
