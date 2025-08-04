import pandas as pd

# Load and validate raw CSV data
class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

# Loads the CSV file into a DataFrame and validates required columns.
    def load_data(self) -> pd.DataFrame:

        df = pd.read_csv(self.file_path)

# Define (set) important columns to ensure they exist in the df.
        required_columns = {"Text", "Biased"}
        missing = required_columns - set(df.columns)
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        return df