
import pandas as pd
import yfinance as yf
from typing import cast


def download_stock_data(tickers, period="5y", interval="1d"):
    """
    Download historical stock data for multiple tickers.

    Parameters:
        tickers: List of stock ticker symbols.
        period: Historical data period.
        interval: Data frequency.

    Returns:
        Combined pandas DataFrame.
    """

    all_data = []

    for ticker in tickers:

        print(f"Downloading data for {ticker}...")

        df = cast(
            pd.DataFrame,
            yf.download(
                ticker,
                period=period,
                interval=interval,
                auto_adjust=True,
                progress=False
            )
        )

        if df.empty:
            print(f"No data found for {ticker}")
            continue

        # Handle MultiIndex columns
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df.reset_index()
        df["Ticker"] = ticker

        all_data.append(df)

    if not all_data:
        raise ValueError("No stock data was downloaded.")

    stock_data = pd.concat(
        all_data,
        ignore_index=True
    )
    
    stock_data = stock_data.sort_values(
        by=["Ticker", "Date"]
    ).reset_index(drop=True)

    return stock_data
