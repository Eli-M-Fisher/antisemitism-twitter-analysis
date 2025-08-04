import pandas as pd
from collections import Counter
from typing import Dict, List

# Analyze the data
class DataAnalyzer:

# 
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

# fun: how many tweets there are from each category (non/antisemitic).
# (Dict[str, int] - Mapping between a string and an integer, for example {"antisemitic": 250})
# value_counts() – Counts distinct occurrences of values in a Biased column
# dropna=False – Requests to include missing values (None or NaN) in the count)
# to_dict() – turns the count result into a dictionary
    def count_by_category(self) -> Dict[str, int]:
        counts = self.df["Biased"].value_counts(dropna=False).to_dict()
        return {
            "antisemitic": counts.get(1, 0),
            "non_antisemitic": counts.get(0, 0),
            "unspecified": counts.get(None, 0) + counts.get("", 0),
            "total": len(self.df)
        }
# counts.get(…) – returns the value of the key if it exists, otherwise 0)


# fun: Counts average length (in words) of tweets (by category and total), creates a dictionary of floats
# Counts on each line [apply(lambda)]; converts text to a string, splits by spaces, and counts words [(str(x).split()].
    def average_length_by_category(self) -> Dict[str, float]:
        self.df["word_count"] = self.df["Text"].apply(lambda x: len(str(x).split()))

        result = {
            "antisemitic": self.df[self.df["Biased"] == 1]["word_count"].mean(),
            "non_antisemitic": self.df[self.df["Biased"] == 0]["word_count"].mean(),
            "total": self.df["word_count"].mean()
        }
        return {k: round(v, 2) for k, v in result.items()}
# average of values [mean()]; rounding to two digits [round(…, 2)]; and looping



    def get_longest_tweets(self, top_n: int = 3) -> Dict[str, List[str]]:
        self.df["length"] = self.df["Text"].apply(lambda x: len(str(x).split()))

        return {
            "antisemitic": self.df[self.df["Biased"] == 1]
                .sort_values(by="length", ascending=False)["Text"]
                .head(top_n).tolist(),

            "non_antisemitic": self.df[self.df["Biased"] == 0]
                .sort_values(by="length", ascending=False)["Text"]
                .head(top_n).tolist()
        }


    def get_top_common_words(self, top_n: int = 10) -> List[str]:
        words = self.df["Text"].dropna().str.cat(sep=" ").split()
        counter = Counter(words)
        return [word for word, _ in counter.most_common(top_n)]


    def count_uppercase_words(self) -> Dict[str, int]:
        def count_upper(words: str) -> int:
            return sum(1 for word in words.split() if word.isupper())

        self.df["uppercase_count"] = self.df["Text"].apply(count_upper)

        return {
            "antisemitic": int(self.df[self.df["Biased"] == 1]["uppercase_count"].sum()),
            "non_antisemitic": int(self.df[self.df["Biased"] == 0]["uppercase_count"].sum()),
            "total": int(self.df["uppercase_count"].sum())
        }
