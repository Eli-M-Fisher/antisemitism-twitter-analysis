import pandas as pd
from collections import Counter
from typing import Dict, List

# Analyze the data
class DataAnalyzer:

# 
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

# fun: how many tweets there are from each category (non/antisemitic).
# (Dict[str, int]: Mapping between a string and an integer, for example {"antisemitic": 250})
# value_counts(): Counts distinct occurrences of values in a Biased column
# dropna=False: Requests to include missing values (None or NaN) in the count)
# to_dict(): turns the count result into a dictionary
    def count_by_category(self) -> Dict[str, int]:
        counts = self.df["Biased"].value_counts(dropna=False).to_dict()
        return {
            "antisemitic": counts.get(1, 0),
            "non_antisemitic": counts.get(0, 0),
            "unspecified": counts.get(None, 0) + counts.get("", 0),
            "total": len(self.df)
        }
# counts.get(…): returns the value of the key if it exists, otherwise 0)
#####



# fun: Counts average length (in words) of tweets (by category and total), creates a dictionary of floats
# Counts on each line [apply(lambda)];
# converts text to a string, splits by spaces, and counts words [(str(x).split()].
    def average_length_by_category(self) -> Dict[str, float]:
        self.df["word_count"] = self.df["Text"].apply(lambda x: len(str(x).split()))

        result = {
            "antisemitic": self.df[self.df["Biased"] == 1]["word_count"].mean(),
            "non_antisemitic": self.df[self.df["Biased"] == 0]["word_count"].mean(),
            "total": self.df["word_count"].mean()
        }
        return {k: round(v, 2) for k, v in result.items()}
# average of values [mean()];
# rounding to two digits [round(…, 2)]; and looping
#####


# fun: Returns the longest tweets in text by category
# Default value [top_n: int = 3] for the number of iterations; dictionary [Dict[str, List[str]]] containing a list of strings for each category
    def get_longest_tweets(self, top_n: int = 3) -> Dict[str, List[str]]:
# Measures the length of each tweet by the number of words
        self.df["length"] = self.df["Text"].apply(lambda x: len(str(x).split()))

        return {
            "antisemitic": self.df[self.df["Biased"] == 1]
                .sort_values(by="length", ascending=False)["Text"]
                .head(top_n).tolist(),

            "non_antisemitic": self.df[self.df["Biased"] == 0]
                .sort_values(by="length", ascending=False)["Text"]
                .head(top_n).tolist()
        }
# (sort_values(…): sorts [sort_values] the rows by length; 
# takes the top N [(head(top_n) - )] (tolist() - converts [(tolist()] the text column to a regular list of strings)
#####


# fun: Finds the most common words in the text
# Returns a list of strings [List[str]] with the most common words;
# removes [(dropna())] missing values in the text;
# Unifies [str.cat(sep=” “)] all texts into one string; splits [split()] into words;
# Counts [Counter(words)] how many times each word appears
# (counter.most_common(top_n): returns the N most common words)
    def get_top_common_words(self, top_n: int = 10) -> List[str]:
        words = self.df["Text"].dropna().str.cat(sep=" ").split()
        counter = Counter(words)
        return [word for word, _ in counter.most_common(top_n)]
#####


# fun: Counts the number of words written in uppercase letters by category
# Counts the [sum(1 for word …)] number of words in which all characters are uppercase;
# [isupper()]: returns True if all letters in the word are uppercase
    def count_uppercase_words(self) -> Dict[str, int]:
        def count_upper(words: str) -> int:
            return sum(1 for word in words.split() if word.isupper())

        self.df["uppercase_count"] = self.df["Text"].apply(count_upper)
# Creates a new column with the number of words in uppercase letters in each tweet
        return {
            "antisemitic": int(self.df[self.df["Biased"] == 1]["uppercase_count"].sum()),
            "non_antisemitic": int(self.df[self.df["Biased"] == 0]["uppercase_count"].sum()),
            "total": int(self.df["uppercase_count"].sum())
        }
# sum(): Sums all uppercase words in all tweets by category
# int(…): Converts to integer, to avoid repetitions like 3.0
#####

