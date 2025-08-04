import pandas as pd
from typing import Optional

# Load and validate raw CSV data
class DataLoader:
    def __init__(self):
        self.file_path = file_path
# Loads the CSV file into a DataFrame and validates required columns.
    def load_data(self):

        df = pd.read_csv(self.file_path)

        required_columns = {"Text", "Biased"}
       