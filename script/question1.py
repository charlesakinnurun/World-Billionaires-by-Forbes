import pandas as pd

# Load the Cleaned DataFrame
df = pd.read_csv("datasets/forbes_cleaned.csv")

# Average of all Billionaires
avg_age = df["Age"].mean()
print(f"The Average age of all Billionaires is : {avg_age:.2f} years")