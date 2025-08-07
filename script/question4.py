import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/forbes_cleaned.csv")

# Youngest Billionaire
youngest_billionaire = df.loc[df["Age"].idxmin()]
print(f"The Youngest Billionaire is {youngest_billionaire["Name"]} with an age of {youngest_billionaire["Age"]} and a networth of ${youngest_billionaire["Net Worth"] /1e9:.2f} B.")