import pandas as pd

def clean_stock_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and validate historical stock market data.

    Parameters:
        df: Raw stock market DataFrame.

    Returns:
        Cleaned stock market DataFrame.
    """
    
    cleaned_data = df.copy()
    
    cleaned_data = cleaned_data.dropna()
    
    # Remove duplicate records for the same stock and date
    cleaned_data = cleaned_data.drop_duplicates(
        subset=["Date", "Ticker"],
        keep="first"
    )
    
    # Remove records with invalid stock prices
    price_columns = ["Open", "High", "Low", "Close"]

    cleaned_data = cleaned_data[
        (cleaned_data[price_columns] > 0).all(axis=1)
    ].copy()
    
    
    # Validate OHLC consistency
    valid_ohlc = (
        (cleaned_data["High"] >= cleaned_data["Open"]) &
        (cleaned_data["High"] >= cleaned_data["Low"]) &
        (cleaned_data["High"] >= cleaned_data["Close"]) &
        (cleaned_data["Low"] <= cleaned_data["Open"]) &
        (cleaned_data["Low"] <= cleaned_data["Close"])
    )

    cleaned_data = cleaned_data[valid_ohlc].copy()
    
    # Remove records with zero or negative trading volume
    cleaned_data = cleaned_data[
        cleaned_data["Volume"] > 0
    ].copy()
    
    # Sort by company and date
    cleaned_data = cleaned_data.sort_values(
        by=["Ticker", "Date"]
    ).reset_index(drop=True)
    

    return cleaned_data