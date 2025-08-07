import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/forbes_cleaned.csv")

# Total net worth from top 3 countries
top_3_countries = df["Country/Territory"].value_counts().head(3).index.to_list()
total_net_worth_top_3 = df[df["Country/Territory"].isin(top_3_countries)]["Net Worth"].sum()
print(f"The total net worth of billionaires from the top 3 countries ({",".join(top_3_countries)}) is ${total_net_worth_top_3 / 1e12:.2f} T.")