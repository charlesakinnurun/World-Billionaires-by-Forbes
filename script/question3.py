import pandas as pd

# Load the Cleaned Data
df = pd.read_csv("datasets/forbes_cleaned.csv")

# Top five most common sources of wealth
top_5_sources = df["Source"].value_counts().head(5)
print(f"The top 5 most common sources of wealth are :")
print(top_5_sources)