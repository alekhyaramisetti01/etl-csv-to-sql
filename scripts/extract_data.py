import pandas as pd

# File path of dataset
csv_file = "../data/sample_movies.csv"  # Change if needed

# Extract step: Read CSV file
def extract_data():
    df = pd.read_csv(csv_file)
    print("✅ Data successfully extracted from CSV!")
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())  # Preview the extracted data
