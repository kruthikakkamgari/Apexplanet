import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load dataset
df = pd.read_csv("business_data.csv")

# Create conversion rate
df["conversion_rate"] = df["conversions"] / df["visits"]

# -----------------------------
# 1. Data Storytelling Insights
# -----------------------------
print("\n--- BUSINESS INSIGHTS ---")

# Average conversion rate by version
avg_conversion = df.groupby("website_version")["conversion_rate"].mean()
print("\nAverage Conversion Rate:")
print(avg_conversion)

# Revenue comparison
avg_revenue = df.groupby("website_version")["revenue"].mean()
print("\nAverage Revenue:")
print(avg_revenue)

# -----------------------------
# 2. Hypothesis Testing
# -----------------------------
print("\n--- HYPOTHESIS TESTING ---")

# Split data
old = df[df["website_version"] == "Old"]["conversion_rate"]
new = df[df["website_version"] == "New"]["conversion_rate"]

# Perform T-test
t_stat, p_value = ttest_ind(new, old)

print(f"T-Statistic: {t_stat}")
print(f"P-Value: {p_value}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Result: Significant improvement with NEW website ✅")
else:
    print("Result: No significant difference ❌")

# -----------------------------
# 3. Visualization
# -----------------------------
plt.figure()
df.groupby("website_version")["conversion_rate"].mean().plot(kind='bar')
plt.title("Conversion Rate Comparison")
plt.ylabel("Conversion Rate")
plt.xlabel("Website Version")
plt.show()

plt.figure()
df.groupby("website_version")["revenue"].mean().plot(kind='bar')
plt.title("Revenue Comparison")
plt.ylabel("Revenue")
plt.xlabel("Website Version")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load dataset
df = pd.read_csv("business_data.csv")

# Create conversion rate
df["conversion_rate"] = df["conversions"] / df["visits"]

# -----------------------------
# 1. Data Storytelling Insights
# -----------------------------
print("\n--- BUSINESS INSIGHTS ---")

# Average conversion rate by version
avg_conversion = df.groupby("website_version")["conversion_rate"].mean()
print("\nAverage Conversion Rate:")
print(avg_conversion)

# Revenue comparison
avg_revenue = df.groupby("website_version")["revenue"].mean()
print("\nAverage Revenue:")
print(avg_revenue)

# -----------------------------
# 2. Hypothesis Testing
# -----------------------------
print("\n--- HYPOTHESIS TESTING ---")

# Split data
old = df[df["website_version"] == "Old"]["conversion_rate"]
new = df[df["website_version"] == "New"]["conversion_rate"]

# Perform T-test
t_stat, p_value = ttest_ind(new, old)

print(f"T-Statistic: {t_stat}")
print(f"P-Value: {p_value}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    result = "Significant improvement with NEW website"
else:
    result = "No significant difference"

print(f"Result: {result}")

# -----------------------------
# 3. Save Output to File
# -----------------------------
content = f"""--- BUSINESS INSIGHTS ---

Average Conversion Rate:
{avg_conversion}

Average Revenue:
{avg_revenue}

--- HYPOTHESIS TESTING ---
T-Statistic: {t_stat}
P-Value: {p_value}

Result: {result}
"""

with open("business_insights.txt", "w") as file:
    file.write(content)

print("\n File saved as 'business_insights.txt'")

# -----------------------------
# 4. Visualization
# -----------------------------
plt.figure()
avg_conversion.plot(kind='bar')
plt.title("Conversion Rate Comparison")
plt.ylabel("Conversion Rate")
plt.xlabel("Website Version")
plt.show()

plt.figure()
avg_revenue.plot(kind='bar')
plt.title("Revenue Comparison")
plt.ylabel("Revenue")
plt.xlabel("Website Version")
plt.show()
