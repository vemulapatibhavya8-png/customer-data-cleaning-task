import pandas as pd
import numpy as np

# Load raw data
df = pd.read_csv("raw_customer_data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df["Customer ID"] = df["Customer ID"].fillna(9999).astype(int)
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].replace("Thirty", np.nan).astype(float)
df["Age"] = df["Age"].fillna(df["Age"].median())

# Standardize gender
df["Gender"] = df["Gender"].str.upper().replace({"F": "FEMALE", "M": "MALE"})

# Standardize country names
df["Country"] = df["Country"].str.upper().replace({
    "UNITED STATES": "USA",
    "UK": "UNITED KINGDOM",
    "U.K.": "UNITED KINGDOM"
})

# Format dates
df["Signup Date"] = pd.to_datetime(df["Signup Date"], dayfirst=True, errors='coerce')
df["Signup Date"] = df["Signup Date"].dt.strftime('%d-%m-%Y')

# Rename columns
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Save cleaned data
df.to_csv("cleaned_customer_data.csv", index=False)
df.to_excel("cleaned_customer_data.xlsx", index=False)
