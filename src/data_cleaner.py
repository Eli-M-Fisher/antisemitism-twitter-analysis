import pandas as pd
import re
import string

# DataCleaner class its role is to clean and process the data
class DataCleaner:

# property of the object to make data copy to store in the class.
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

# clears a single text
    def clean_text(self):
        
# Removes rows that do not have valid values in the Biased column
    def remove_unspecified_rows(self) -> pd.DataFrame:

# Central all cleaning steps: filters rows, cleans text, and returns a clean table
    def clean_dataset(self) -> pd.DataFrame:


        return
