import pandas as pd


def data_set(path):
    """
    Load and clean data from a CSV file located at the specified path. The function handles missing data,
    corrects data types, and manages date formatting issues.

    Args:
        path (str): The file path of the CSV file to be loaded.

    Returns:
        DataFrame: A pandas DataFrame containing cleaned and processed data from the CSV file.

    This function performs the following operations:
    - Fills missing entries in 'customer_name' with 'Unknown' and 'feedback_text' with 'No feedback.'.
    - Attempts to convert 'feedback_id' to integers, replacing non-convertible values with -1.
    - Tries to parse 'submission_date' according to a specified date format, falling back to a day-first format if the initial parsing fails.
    - Any remaining missing or incorrectly formatted dates are filled with a default early date (January 1, 1900).
    """

    df = pd.read_csv(path)

    # Handle missing string data
    df['customer_name'] = df['customer_name'].fillna('Unknown')
    df['feedback_text'] = df['feedback_text'].fillna('No feedback.')

    # Convert 'feedback_id' to integer, handle non-numeric with -1
    df['feedback_id'] = pd.to_numeric(df['feedback_id'], errors='coerce').fillna(-1).astype(int)

    # Handle date parsing with a try-except block
    try:
        df['submission_date'] = pd.to_datetime(df['submission_date'], format='%d/%m/%Y', errors='coerce')
    except ValueError:
        # If the format fails, parse with day-first assumption
        df['submission_date'] = pd.to_datetime(df['submission_date'], dayfirst=True, errors='coerce')

    # Set a default date for any remaining missing or unparsable dates
    default_date = pd.Timestamp('1900-01-01')
    df['submission_date'] = df['submission_date'].fillna(default_date)

    return df
