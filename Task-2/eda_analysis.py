import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('employee_performance.csv')

# Bar Chart
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
dept_perf = df.groupby('Department')['Performance_Rating'].mean().sort_values()
sns.barplot(x=dept_perf.index, y=dept_perf.values, palette='viridis')
plt.title('Average Performance Rating by Department')

# Pie Chart
plt.subplot(2, 2, 2)
rating_counts = df['Performance_Rating'].value_counts().sort_index()
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Performance Rating Distribution')

# Correlation Heatmap
plt.subplot(2, 2, 3)
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')

# Line Chart
plt.subplot(2, 2, 4)
exp_salary = df.groupby('Experience_Years')['Monthly_Salary'].mean().reset_index()
plt.plot(exp_salary['Experience_Years'], exp_salary['Monthly_Salary'], marker='o', color='orange')
plt.title('Average Salary vs Experience')

plt.tight_layout()
plt.show()
