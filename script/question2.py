import pandas as pd

# Load the cleaned DataFrame
df = pd.read_csv("datasets/forbes_cleaned.csv")

# Country with the Highest number of Billionaires
most_billionaires_country = df["Country/Territory"].value_counts().idxmax()
num_billionaires = df["Country/Territory"].value_counts().max()
print(f"The Country with the highest number of Billionaires is : {most_billionaires_country}")