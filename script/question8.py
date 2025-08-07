import pandas as pd

# Load the cleaned data
df = pd.read_csv("datasets/forbes_cleaned.csv")

# Person with the highest change in net worth
highest_change_person = df.loc[df["Change"].idxmax()]
print(f"The person with the highest change in net worth is {highest_change_person["Name"]} with a change of ${highest_change_person["Change"] / 1e9:.2f} B.")