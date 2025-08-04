from pathlib import Path

from data_loader import DataLoader
from data_cleaner import DataCleaner
from data_analyzer import DataAnalyzer
from result_writer import ResultWriter


def main():
    # Define base directory and file paths
    base_dir = Path(__file__).resolve().parent.parent
    input_path = base_dir / "data" / "tweets_dataset.csv"
    cleaned_csv_path = base_dir / "results" / "tweets_dataset_cleaned.csv"
    json_result_path = base_dir / "results" / "results.json"

    # Ensure results folder exists
    (base_dir / "results").mkdir(parents=True, exist_ok=True)

    print("[INFO] Loading data...")
    loader = DataLoader(str(input_path))
    raw_df = loader.load_data()

    print("[INFO] Counting uppercase words (before cleaning)...")
    uppercase_counts = DataAnalyzer(raw_df).count_uppercase_words()

    print("[INFO] Cleaning data...")
    cleaner = DataCleaner(raw_df)
    cleaned_df = cleaner.clean_dataset()

    print("[INFO] Analyzing cleaned data...")
    analyzer = DataAnalyzer(cleaned_df)
    analysis_results = {
        "total_tweets": analyzer.count_by_category(),
        "average_length": analyzer.average_length_by_category(),
        "common_words": {"total": analyzer.get_top_common_words()},
        "longest_3_tweets": analyzer.get_longest_tweets(),
        "uppercase_words": uppercase_counts  # From raw data
    }

    print("[INFO] Writing results...")
    writer = ResultWriter(cleaned_df, analysis_results)
    writer.save_cleaned_csv(str(cleaned_csv_path))
    writer.save_analysis_json(str(json_result_path))

    print("[SUCCESS] All steps completed. Results saved in 'results/' directory.")


if __name__ == "__main__":
    main()