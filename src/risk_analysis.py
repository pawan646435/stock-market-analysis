
import pandas as pd


def calculate_daily_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate daily percentage returns for each stock.

    Parameters:
        df: Cleaned stock market DataFrame.

    Returns:
        DataFrame containing daily returns.
    """

    data = df.copy()

    data["Daily_Return"] = (
        data.groupby("Ticker")["Close"]
        .pct_change() * 100
    )

    return data


import numpy as np


def calculate_annualized_volatility(df: pd.DataFrame) -> pd.Series:
    """
    Calculate annualized volatility for each stock.

    Parameters:
        df: DataFrame containing Daily_Return.

    Returns:
        Annualized volatility for each ticker.
    """

    daily_volatility = (
        df.groupby("Ticker")["Daily_Return"].std()
    )

    annualized_volatility = daily_volatility * np.sqrt(252)

    return annualized_volatility


def calculate_annualized_return(df: pd.DataFrame) -> pd.Series:
    """
    Calculate annualized arithmetic mean return for each stock.

    Parameters:
        df: DataFrame containing Daily_Return.

    Returns:
        Annualized mean return for each ticker.
    """

    daily_mean_return = (
        df.groupby("Ticker")["Daily_Return"].mean()
    )

    annualized_return = daily_mean_return * 252

    return annualized_return


def calculate_cagr(df: pd.DataFrame) -> pd.Series:
    """
    Calculate CAGR for each stock using its first and last closing prices.

    Parameters:
        df: Cleaned stock DataFrame containing Date, Ticker and Close.

    Returns:
        CAGR percentage for each ticker.
    """

    results = {}

    for ticker, group in df.groupby("Ticker"):

        group = group.sort_values("Date")

        beginning_value = group["Close"].iloc[0]
        ending_value = group["Close"].iloc[-1]

        period_years = (
            group["Date"].iloc[-1] - group["Date"].iloc[0]
        ).days / 365.25

        cagr = (
            (ending_value / beginning_value) ** (1 / period_years) - 1
        ) * 100

        results[ticker] = cagr

    return pd.Series(results, name="CAGR_Percent")



def calculate_sharpe_ratio(
    df: pd.DataFrame,
    risk_free_rate: float = 0.0
) -> pd.Series:
    """
    Calculate the annualized Sharpe ratio for each stock.

    Parameters:
        df: DataFrame containing Daily_Return.
        risk_free_rate: Annual risk-free rate in percentage units.

    Returns:
        Sharpe ratio for each ticker.
    """

    daily_mean_return = (
        df.groupby("Ticker")["Daily_Return"].mean()
    )

    daily_volatility = (
        df.groupby("Ticker")["Daily_Return"].std()
    )

    annualized_return = daily_mean_return * 252

    annualized_volatility = daily_volatility * np.sqrt(252)

    sharpe_ratio = (
        (annualized_return - risk_free_rate)
        / annualized_volatility
    )

    return sharpe_ratio.rename("Sharpe_Ratio")



def generate_risk_report(
    df: pd.DataFrame,
    risk_free_rate: float = 0.0
) -> pd.DataFrame:
    """
    Generate a consolidated risk and return report for all stocks.
    """

    returns_data = calculate_daily_returns(df)

    annualized_return = calculate_annualized_return(returns_data)
    annualized_volatility = calculate_annualized_volatility(returns_data)
    cagr = calculate_cagr(df)
    sharpe = calculate_sharpe_ratio(returns_data, risk_free_rate)

    report = pd.DataFrame({
        "Annualized_Return": annualized_return,
        "Annualized_Volatility": annualized_volatility,
        "CAGR": cagr,
        "Sharpe_Ratio": sharpe
    })

    report = report.sort_values(
        by="CAGR",
        ascending=False
    )

    return report



def calculate_return_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate daily return statistics for each stock.

    Parameters:
        df: DataFrame containing Ticker and Daily_Return columns.

    Returns:
        DataFrame containing mean, volatility,
        maximum and minimum daily returns.
    """

    
    risk_return = df.groupby("Ticker").agg(
        Mean_Return=("Daily_Return", "mean"),
        Volatility=("Daily_Return", "std"),
        Maximum_Return=("Daily_Return", "max"),
        Minimum_Return=("Daily_Return", "min")
    )

    return risk_return

