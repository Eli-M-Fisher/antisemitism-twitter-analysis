import pandas as pd
import json
from typing import Dict

# class: Responsible for writing cleaned dataset and analysis results to files.
# This is a utility class that does not analyze data itself, but rather saves results to files.
class ResultWriter:
        # cleaned_df: pd.DataFrame: a clean data table, of type pandas DataFrame
        # analysis_results: Dict: a dictionary of analysis results.
    def __init__(self, cleaned_df: pd.DataFrame, analysis_results: Dict):
        # self.cleaned_df: Object attribute: Holds the table for internal use
        # self.analysis_results: Additional attribute: Holds the captured analysis results
        self.cleaned_df = cleaned_df
        self.analysis_results = analysis_results


    # Saves the cleaned dataset to a CSV file.
    # path: str: the path (as a string)
    # [[[[-> None: annotation the function does not return a value, but performs an action]]]]
    def save_cleaned_csv(self, path: str) -> None:
        self.cleaned_df.to_csv(path, index=False)

        

    # Saves the analysis results to a JSON file.
    def save_analysis_json(self, path: str) -> None:
        
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.analysis_results, f, indent=4, ensure_ascii=False)
        # Open file [with open(…) as f] for safe writing: auto-close when finished; “w” write mode.
        # encoding=“utf-8”: Text to support all languages
