import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/forbes_cleaned.csv")

# US Billionaires count and total net worth
us_billionaires = df[df["Country/Territory"] == "United States"]
us_count = len(us_billionaires)
us_total_net_worth = us_billionaires["Net Worth"].sum()
print(f"There are {us_count} billionaires from the United States with a total Net Worth of {us_total_net_worth / 1e12:.2f} T.")