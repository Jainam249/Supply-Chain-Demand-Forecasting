"""
Anomaly Detection Module

This module provides reusable functions for detecting anomalies
using statistical and machine learning techniques.
"""

import pandas as pd
from scipy.stats import zscore
from sklearn.ensemble import IsolationForest


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

    result = df.copy()

    result["z_score"] = zscore(result[column])

    result["z_anomaly"] = result["z_score"].abs() > threshold

    return result


def detect_iqr(df, column="sales"):
    """
    Detect anomalies using the Interquartile Range (IQR).

    Parameters:
        df (DataFrame): Input DataFrame
        column (str): Column to analyze

    Returns:
        DataFrame
    """

    result = df.copy()

    q1 = result[column].quantile(0.25)
    q3 = result[column].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - (1.5 * iqr)
    upper = q3 + (1.5 * iqr)

    result["iqr_anomaly"] = (result[column] < lower) | (result[column] > upper)

    return result


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

    result = df.copy()

    model = IsolationForest(contamination=contamination, random_state=random_state)

    result["iforest"] = model.fit_predict(result[[column]])

    result["iforest_anomaly"] = result["iforest"] == -1

    return result
