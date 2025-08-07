import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/forbes_cleaned.csv")

# Average net worth of billionaires by Country
avg_net_worth_by_country = df.groupby("Country/Territory")["Net Worth"].mean().sort_values(ascending=False).head()
print("The top 5 countries by average net worth are :")
print(avg_net_worth_by_country)