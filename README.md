# Forbes World's Billionaires Analysis

![Forbes](assets/forbes.jpg)

This project analyzes the Forbes World's Billionaires list to extract insights and answer specific questions about the world's wealthiest individuals.

## Dataset

The project uses two datasets:

- `datasets/forbes.csv`: The raw data scraped from Forbes.
- `datasets/forbes_cleaned.csv`: The cleaned and preprocessed data used for analysis.

## Data Cleaning

The `script/cleaning.py` script performs the following data cleaning and preprocessing steps:

- **Currency Conversion:** Converts the 'Net Worth', and 'Change' columns from string format (e.g., "$177B", "$1.2M") to numeric format (in dollars).
- **Percentage Cleaning:** Removes the '%' symbol from the 'Percentage Change' column and converts it to a numeric type.
- **String Standardization:** Trims leading/trailing whitespace from the 'Source' and 'Country/Territory' columns.

The cleaned data is saved to `datasets/forbes_cleaned.csv`.

## Analysis Questions

The `script/` directory contains Python scripts to answer the following questions:

- `question1.py`: What is the average age of all billionaires?
- `question2.py`: Which country has the highest number of billionaires?
- `question3.py`: Who is the richest billionaire?
- `question4.py`: Who is the youngest and oldest billionaire?
- `question5.py`: Which source of wealth is the most common?
- `question6.py`: How many billionaires are there in each age group?
- `question7.py`: What is the average net worth of billionaires by country?
- `question8.py`: Who are the top 10 richest billionaires?
- `question9.py`: What is the distribution of billionaires by gender?
- `question10.py`: What is the correlation between age and net worth?

## How to Run the Scripts

1.  **Prerequisites:** Make sure you have Python and the required libraries installed.
    ```bash
    pip install pandas
    ```

2.  **Run the cleaning script:**
    ```bash
    python script/cleaning.py
    ```

3.  **Run an analysis script:**
    ```bash
    python script/question1.py
    ```

## Project Structure
```
.
├── assets
│   └── forbes.jpg
├── datasets
│   ├── forbes.csv
│   └── forbes_cleaned.csv
├── script
│   ├── cleaning.py
│   ├── question1.py
│   ├── question10.py
│   ├── question2.py
│   ├── question3.py
│   ├── question4.py
│   ├── question5.py
│   ├── question6.py
│   ├── question7.py
│   ├── question8.py
│   └── question9.py
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

