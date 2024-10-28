import pandas as pd
import os

clean_data_directory = os.path.join(os.path.dirname(__file__), "clean_data")


# Load your CSV file into a DataFrame
df = pd.read_csv('univariate/evaluations/rmse.csv')

# Assuming the first column is the key, get its column name
key_column = df.columns[0]

# Remove succeeding duplicates based on the first column
df_no_duplicates = df.drop_duplicates(subset=[key_column], keep='first')

df_no_duplicates.to_csv(os.path.join(clean_data_directory, "rmse.csv"), index=False)

