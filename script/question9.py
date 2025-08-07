import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/forbes_cleaned.csv")

# List of all billionaires under the age of 40
billionaires_under_40 = df[df["Age"] < 40][["Name","Age","Net Worth","Country/Territory"]]
print(billionaires_under_40)