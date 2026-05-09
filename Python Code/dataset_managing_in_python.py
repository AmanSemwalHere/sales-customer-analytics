import pandas as pd
import numpy as np

# Loading the dataset
df = pd.read_csv("updated_online_retail.csv")

np.random.seed(42)

# 1. Discount column
df["Discount (%)"] = np.round(np.random.uniform(0, 20, len(df)), 2)

# 2. Shipping cost
df["Shipping_Cost"] = np.where(df["Country"] == "United Kingdom",
                               np.round(np.random.uniform(2, 5, len(df)), 2),
                               np.round(np.random.uniform(5, 15, len(df)), 2))

# 3. Customer Segment
conditions = [
    df["Monetary"] < df["Monetary"].quantile(0.33),
    df["Monetary"] < df["Monetary"].quantile(0.66)
]
choices = ["Low Value", "Mid Value"]

df["Customer_Segment"] = np.select(conditions, choices, default="High Value")

# Saving the file
df.to_csv("updated_dataset.csv", index=False)
print("Done! File saved as updated_dataset.csv")
