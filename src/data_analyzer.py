import pandas as pd
from collections import Counter
from typing import Dict, List

class DataAnalyzer:


    def __init__(self, df: pd.DataFrame):
        return

    def count_by_category(self) -> Dict[str, int]:
        return

    def average_length_by_category(self) -> Dict[str, float]:
        return

    def get_longest_tweets(self, top_n: int = 3) -> Dict[str, List[str]]:
        return

    def get_top_common_words(self, top_n: int = 10) -> List[str]:
        return

    def count_uppercase_words(self) -> Dict[str, int]:
        return
