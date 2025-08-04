import pandas as pd
import re
import string

# DataCleaner class its role is to clean and process the data
class DataCleaner:

# property of the object to make data copy to store in the class.
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

# clears a single text
    def clean_text(self, text: str) -> str:

        if not isinstance(text, str):
            return ""
        
        # Remove punctuation
        text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
        # Convert to lowercase
        text = text.lower()
        return text
        
# Removes rows that do not have valid values in the Biased column
    def remove_unspecified_rows(self) -> pd.DataFrame:

        return self.df[self.df["Biased"].isin([0, 1])]


# Central all cleaning steps: filters rows, cleans text, and returns a clean table
    def clean_dataset(self) -> pd.DataFrame:

        df_filtered = self.remove_unspecified_rows()
        df_filtered["Text"] = df_filtered["Text"].apply(self.clean_text)
        return df_filtered[["Text", "Biased"]].reset_index(drop=True)