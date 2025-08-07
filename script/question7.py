import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/forbes_cleaned.csv")

# Median age of Billionaires from China vs Us
china_median_age = df[df["Country/Territory"] == "China"]["Age"].median()
us_median_age = df[df["Country/Territory"] == "United States"]["Age"].median()
print(f"The median age of billionaires from china is {china_median_age} years, while the median age of billionaires from us is {us_median_age} years")