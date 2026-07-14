"""
Evaluation Module

Reusable model evaluation functions.
"""

import numpy as np
from sklearn.metrics import (
    mean_squared_error,
    mean_absolute_error,
    mean_absolute_percentage_error,
)


def calculate_rmse(actual, predicted):
    """
    Calculate Root Mean Squared Error.
    """

    return np.sqrt(mean_squared_error(actual, predicted))


def calculate_mae(actual, predicted):
    """
    Calculate Mean Absolute Error.
    """

    return mean_absolute_error(actual, predicted)


def calculate_mape(actual, predicted):
    """
    Calculate Mean Absolute Percentage Error.
    """

    return mean_absolute_percentage_error(actual, predicted)


def evaluate_model(actual, predicted):
    """
    Return all evaluation metrics.
    """

    results = {
        "RMSE": calculate_rmse(actual, predicted),
        "MAE": calculate_mae(actual, predicted),
        "MAPE": calculate_mape(actual, predicted),
    }

    return results
