import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose


def load_dataset(path):
    """Load the supply chain dataset."""
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df


def remove_duplicates(df):
    """Remove duplicate rows."""
    return df.drop_duplicates()


def sort_dates(df):
    """Sort records by date."""
    return df.sort_values("date")


def set_datetime_index(df):
    """Set the date column as the DataFrame index."""
    return df.set_index("date")


def check_missing_values(df):
    """Return missing values by column."""
    return df.isnull().sum()


def resample_sales(df, frequency="M"):
    """Aggregate sales at a specified frequency."""
    return df["sales"].resample(frequency).sum()


def perform_decomposition(series, model="additive", period=12):
    """Perform seasonal decomposition."""
    return seasonal_decompose(series, model=model, period=period)
