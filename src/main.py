from pathlib import Path

from data_loader import DataLoader
from data_cleaner import DataCleaner
from data_analyzer import DataAnalyzer
from result_writer import ResultWriter

def main():
    # Define paths
    base_dir = Path(__file__).resolve().parent.parent
    input_path = base_dir / "data" / "tweets_dataset.csv"
    cleaned_csv_path = base_dir / "results" / "tweets_dataset_cleaned.csv"
    json_result_path = base_dir / "results" / "results.json"

    # Load data
    # TODO: Create DataLoader and load raw DataFrame

    # Clean data
    # TODO: Use DataCleaner to clean raw DataFrame

    # Analyze data
    # TODO: Use DataAnalyzer to extract statistical and text features

    # Save results
    # TODO: Save cleaned DataFrame and analysis results using ResultWriter

    # Final message
    # TODO: Print success message


# ===== Entrypoint =====
if __name__ == "__main__":
    main()