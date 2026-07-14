"""
Forecasting Module

Reusable forecasting functions for the Supply Chain Demand
Forecasting project.
"""

import numpy as np
import pandas as pd
from collections import deque


from statsmodels.tsa.arima.model import ARIMA


def train_test_split_time_series(df, train_size=0.8):
    """
    Split a time-series dataset into train and test sets.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe.

    train_size : float
        Fraction of data to use for training.

    Returns
    -------
    train : DataFrame
    test : DataFrame
    """

    split_index = int(len(df) * train_size)

    train = df.iloc[:split_index]

    test = df.iloc[split_index:]

    return train, test


def moving_average_forecast(train, test, column="sales", window=7):
    """
    Forecast using a simple moving average.

    Parameters
    ----------
    train : DataFrame

    test : DataFrame

    column : str

    window : int

    Returns
    -------
    list
        Forecast values.
    """

    history = deque(
        train[column].tail(window).to_numpy(dtype=np.float64), maxlen=window
    )

    test_values = test[column].to_numpy(dtype=np.float64)
    predictions = np.empty(len(test_values), dtype=np.float64)

    for i, actual in enumerate(test_values):
        predictions[i] = np.mean(history)
        history.append(actual)

    return predictions


def train_arima(train, column="sales", order=(5, 1, 0)):
    """
    Train an ARIMA model.

    Returns
    -------
    Fitted ARIMA model.
    """

    model = ARIMA(train[column], order=order)

    return model.fit()


def arima_forecast(model, steps):
    """
    Forecast future observations.

    Parameters
    ----------
    model : fitted ARIMA model

    steps : int

    Returns
    -------
    Forecast values
    """

    return model.forecast(steps=steps)


def forecast_future(df, column="sales", periods=90, order=(5, 1, 0)):
    """
    Forecast future demand.

    Parameters
    ----------
    df : DataFrame

    periods : int

    Returns
    -------
    Forecast DataFrame
    """

    model = ARIMA(df[column], order=order)

    fitted_model = model.fit()

    forecast = fitted_model.forecast(steps=periods)

    future_dates = pd.date_range(
        start=df.index[-1] + pd.Timedelta(days=1), periods=periods, freq="D"
    )

    forecast_df = pd.DataFrame({"date": future_dates, "forecast_sales": forecast})

    return forecast_df
