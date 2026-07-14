"""
Anomaly Detection Module

This module provides reusable functions for detecting anomalies
using statistical and machine learning techniques.
"""

import pandas as pd
from scipy.stats import zscore
from sklearn.ensemble import IsolationForest
from scipy.stats import zscore


def detect_zscore(df, column="sales", threshold=3):
    """
    Detect anomalies using the Z-Score method.

    Parameters:
        df (DataFrame): Input DataFrame
        column (str): Column to analyze
        threshold (float): Z-score threshold

    Returns:
        DataFrame
    """

    df["z_score"] = zscore(df[column].values)

    df["z_anomaly"] = df["z_score"].abs() > threshold

    return df


def detect_iqr(df, column="sales", factor=1.5):
    """
    Detect anomalies using the Interquartile Range (IQR).

    Parameters:
        df (DataFrame): Input DataFrame
        column (str): Column to analyze

    Returns:
        DataFrame
    """

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - factor * IQR
    upper_bound = Q3 + factor * IQR

    df["iqr_anomaly"] = (df[column] < lower_bound) | (df[column] > upper_bound)

    return df


def detect_isolation_forest(df, column="sales", contamination=0.01, random_state=42):
    """
    Detect anomalies using Isolation Forest.

    Parameters:
        df (DataFrame): Input DataFrame
        column (str): Column to analyze
        contamination (float): Expected anomaly proportion
        random_state (int): Random seed

    Returns:
        DataFrame
    """

    model = IsolationForest(
        contamination=contamination,
        random_state=random_state,
        n_estimators=100,
        n_jobs=-1,
    )

    # Train using a sample
    sample_size = min(200000, len(df))

    train_data = df[[column]].sample(sample_size, random_state=random_state)

    model.fit(train_data)

    # Predict in batches to avoid large memory usage
    batch_size = 100000
    predictions = []

    for start in range(0, len(df), batch_size):
        batch = df[[column]].iloc[start : start + batch_size]
        predictions.extend(model.predict(batch))

    df["iforest"] = predictions
    df["iforest_anomaly"] = df["iforest"] == -1

    return df
