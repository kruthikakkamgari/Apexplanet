import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# Customer Segmentation
def segment_customer(amount):
    if amount >= 50000:
        return "High Value"
    elif amount >= 20000:
        return "Medium Value"
    else:
        return "Low Value"

df["customer_segment"] = df["total_purchase_amount"].apply(segment_customer)

# Segment distribution
print("Customer Segment Distribution:")
print(df["customer_segment"].value_counts())

# Save segmented data
df.to_csv("segmented_data.csv", index=False)

print("\nSegmented data saved as segmented_data.csv")
