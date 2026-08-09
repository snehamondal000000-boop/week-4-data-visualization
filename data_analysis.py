import pandas as pd

# Load dataset
file_path = "Sample data (1) (1).xlsx"
df = pd.read_excel(file_path)
df.columns = df.columns.str.strip()

# Basic information
print("===== DATASET INFORMATION =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nColumns:")
print(df.columns.tolist())

# Data types
print("\n===== DATA TYPES =====")
print(df.dtypes)

# Missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Fill missing Discount Band
df["Discount Band"] = df["Discount Band"].fillna("Unknown")

# Duplicate check
print("\n===== DUPLICATES =====")
print("Duplicate rows:", df.duplicated().sum())

# Business metrics
print("\n===== BUSINESS METRICS =====")
print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Total Units Sold:", df["Units Sold"].sum())

# Sales by Country
print("\n===== SALES BY COUNTRY =====")
print(df.groupby("Country")["Sales"].sum().sort_values(ascending=False))

# Sales by Product
print("\n===== SALES BY PRODUCT =====")
print(df.groupby("Product")["Sales"].sum().sort_values(ascending=False))

# Profit by Product
print("\n===== PROFIT BY PRODUCT =====")
print(df.groupby("Product")["Profit"].sum().sort_values(ascending=False))

# Sales by Year
print("\n===== SALES BY YEAR =====")
print(df.groupby("Year")["Sales"].sum().sort_values(ascending=False))

# Sales by Segment
print("\n===== SALES BY SEGMENT =====")
print(df.groupby("Segment")["Sales"].sum().sort_values(ascending=False))

print("\n===== ANALYSIS COMPLETED =====")