import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("cleaned_data.csv")

print("Dataset Loaded Successfully!\n")
print(df.head())

# -------------------------------
# 2. Customer Segmentation
# -------------------------------
def segment_customer(amount):
    if amount >= 50000:
        return "High Value"
    elif amount >= 20000:
        return "Medium Value"
    else:
        return "Low Value"

df["customer_segment"] = df["total_purchase_amount"].apply(segment_customer)

# -------------------------------
# 3. KPI Calculations
# -------------------------------
total_revenue = df["total_purchase_amount"].sum()
average_purchase = df["total_purchase_amount"].mean()
total_customers = df.shape[0]

print("\n📊 KPI Metrics:")
print("Total Revenue:", total_revenue)
print("Average Purchase Value:", average_purchase)
print("Total Customers:", total_customers)

# -------------------------------
# 4. Segment Distribution
# -------------------------------
print("\nCustomer Segment Distribution:")
segment_counts = df["customer_segment"].value_counts()
print(segment_counts)

# -------------------------------
# 5. Segment-wise Analysis
# -------------------------------
segment_analysis = df.groupby("customer_segment")["total_purchase_amount"].agg(
    ["count", "mean", "sum"]
)

print("\nSegment-wise Analysis:")
print(segment_analysis)

# -------------------------------
# 6. Save Outputs (Dashboard Ready)
# -------------------------------
df.to_csv("segmented_data.csv", index=False)
segment_analysis.to_csv("segment_analysis.csv")

kpi_df = pd.DataFrame({
    "Metric": ["Total Revenue", "Average Purchase", "Total Customers"],
    "Value": [total_revenue, average_purchase, total_customers]
})
kpi_df.to_csv("kpi_metrics.csv", index=False)

print("\n✅ Files Saved:")
print("- segmented_data.csv")
print("- segment_analysis.csv")
print("- kpi_metrics.csv")

# -------------------------------
# 7. Visualization
# -------------------------------

# Bar Chart - Segment Distribution
plt.figure()
segment_counts.plot(kind='bar')
plt.title("Customer Segment Distribution")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")
plt.show()

# Pie Chart - Segment Share
plt.figure()
segment_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Customer Segment Share")
plt.ylabel("")
plt.show()

# Revenue by Segment
plt.figure()
segment_analysis["sum"].plot(kind='bar')
plt.title("Revenue by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Total Revenue")
plt.show()

print("\n🎯 Analysis Complete! Ready for Dashboard Integration.")
