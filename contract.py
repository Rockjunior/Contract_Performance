import pandas as pd

# Sample data
data = {
    'Employee ID': ['E001', 'E002', 'E003', 'E004', 'E005']*10,
    'Month': ['Jan', 'Jan', 'Jan', 'Jan', 'Jan',
              'Feb', 'Feb', 'Feb', 'Feb', 'Feb',
              'Mar', 'Mar', 'Mar', 'Mar', 'Mar',
              'Apr', 'Apr', 'Apr', 'Apr', 'Apr',
              'May', 'May', 'May', 'May', 'May',
              'Jun', 'Jun', 'Jun', 'Jun', 'Jun',
              'Jul', 'Jul', 'Jul', 'Jul', 'Jul',
              'Aug', 'Aug', 'Aug', 'Aug', 'Aug',
              'Sep', 'Sep', 'Sep', 'Sep', 'Sep',
              'Oct', 'Oct', 'Oct', 'Oct', 'Oct'],
    'Monthly Revenue': [105000, 98000, 120000, 93000, 110000, 102000, 99000, 118000, 95000, 112000, 108000, 97000, 121000, 92000, 115000, 107000, 96000, 119000, 94000, 113000, 104000, 95000, 122000, 91000, 116000, 106000, 94000, 123000, 93000, 117000, 109000, 96000, 124000, 92000, 114000, 105000, 97000, 125000, 94000, 118000, 107000, 95000, 121000, 93000, 116000, 106000, 96000, 122000, 92000, 115000],
    'Number of New Clients': [12, 8, 15, 9, 11, 10, 7, 13, 10, 12, 11, 9, 14, 8, 13, 12, 8, 16, 9, 14, 10, 9, 15, 8, 13, 11, 8, 14, 7, 12, 13, 9, 16, 8, 14, 12, 7, 15, 10, 13, 11, 9, 14, 8, 12, 10, 8, 13, 7, 11],
    'Customer Satisfaction Score': [87, 82, 90, 85, 88, 86, 80, 91, 83, 89, 84, 78, 92, 82, 90, 85, 79, 89, 84, 87, 88, 81, 90, 86, 91, 89, 82, 93, 85, 88, 87, 83, 91, 80, 89, 86, 81, 92, 87, 90, 85, 84, 90, 83, 89, 88, 82, 91, 80, 87]
}

df = pd.DataFrame(data)

# Normalization
df['Norm Revenue'] = (df['Monthly Revenue'] - df['Monthly Revenue'].min()) / (df['Monthly Revenue'].max() - df['Monthly Revenue'].min())
df['Norm Clients'] = (df['Number of New Clients'] - df['Number of New Clients'].min()) / (df['Number of New Clients'].max() - df['Number of New Clients'].min())
df['Norm Satisfaction'] = (df['Customer Satisfaction Score'] - df['Customer Satisfaction Score'].min()) / (df['Customer Satisfaction Score'].max() - df['Customer Satisfaction Score'].min())

# Weighting
weights = {'Norm Revenue': 0.50, 'Norm Clients': 0.30, 'Norm Satisfaction': 0.20}
df['Total Score'] = df['Norm Revenue'] * weights['Norm Revenue'] + df['Norm Clients'] * weights['Norm Clients'] + df['Norm Satisfaction'] * weights['Norm Satisfaction']

# Grading
def assign_grade(score):
    if score >= 0.90:
        return 'A'
    elif score >= 0.80:
        return 'B'
    elif score >= 0.70:
        return 'C'
    elif score >= 0.60:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Total Score'].apply(assign_grade)

# Display the first few rows of the DataFrame
print(df[['Employee ID', 'Month', 'Monthly Revenue', 'Number of New Clients', 'Customer Satisfaction Score', 'Total Score', 'Grade']].head(10))
