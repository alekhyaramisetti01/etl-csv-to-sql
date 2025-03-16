import pandas as pd
from extract_data import extract_data

# Transform step: Clean and preprocess data
def transform_data(df):
    df = df.drop_duplicates()  # Remove duplicate rows
    df = df.dropna()  # Remove missing values
    df['title'] = df['title'].str.title()  # Standardize title format (Title Case)
    df['genre'] = df['genre'].str.lower()  # Convert genre to lowercase
    df['year'] = df['year'].astype(int)  # Ensure 'year' is an integer
    df['rating'] = df['rating'].astype(float)  # Ensure 'rating' is a float
    print("✅ Data successfully transformed!")
    return df

if __name__ == "__main__":
    df = extract_data()  # Call extract step
    df_transformed = transform_data(df)
    print(df_transformed.head())  # Preview transformed data
