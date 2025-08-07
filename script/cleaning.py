import pandas as pd

# Load the DataFrame
df = pd.read_csv("datasets/forbes.csv")

# Function to clean currency values
def clean_currency(value):
    if pd.isna(value) or value == "0M":
        return 0.0
    value = str(value).replace("$","").strip()
    if "B" in value:
        value = float(value.replace("B","").strip()) * 1e9
    elif "M" in value:
        value = float(value.replace("M","").strip()) * 1e6
    elif value.endswith("M"):
        value = float(value.replace("M","").strip()) * 1e6
    elif  value == "0":
        return 0.0
    return float(value)

# Apply the function to the 'Net Worth' and 'Change' columns
df["Net Worth"] = df["Net Worth"].apply(clean_currency)
df["Change"] = df["Change"].apply(clean_currency)

# Clean the 'Percentage Change' column
df["Percentage Change"] = df["Percentage Change"].str.replace("%","",regex=False)
df["Percentage Change"] = pd.to_numeric(df["Percentage Change"],errors="coerce")

# Standardize the 'Source' and 'Country/Territory' columns
df["Source"] = df["Source"].str.strip()
df["Country/Territory"] = df["Country/Territory"].str.strip()

# Display the first 5 rows and the info of the DataFrame
print(df.head())
print(df.info())

# Save the Cleaned DataFrame to a new CSV file
df.to_csv("datasets/forbes_cleaned.csv",index=False)
print("The Cleaned Data has been created successfuly")