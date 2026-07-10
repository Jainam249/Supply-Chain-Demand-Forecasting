import pandas as pd


def load_dataset(path):
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df


def remove_duplicates(df):
    return df.drop_duplicates()


def sort_dates(df):
    return df.sort_values("date")


def set_datetime_index(df):
    return df.set_index("date")


def resample_sales(df, frequency="M"):
    return df["sales"].resample(frequency).sum()
