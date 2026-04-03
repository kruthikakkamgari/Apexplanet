
import pandas as pd

data = pd.read_csv("customer_sales_raw_large.csv")

data["Customer_Name"] = data["Customer_Name"].fillna("Not Available")
data = data.drop_duplicates()

data["Order_Date"] = pd.to_datetime(data["Order_Date"], errors="coerce")
data = data.dropna(subset=["Order_Date"])

data["Total_Price"] = data["Quantity"] * data["Unit_Price"]

data.to_csv("customer_sales_cleaned_large.csv", index=False)

print("Cleaning Done Successfully")
