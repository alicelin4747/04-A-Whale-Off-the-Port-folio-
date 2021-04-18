import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path
import seaborn as sns


def main():
    whale_returns_path = Path("Resources/whale_returns.csv")
    whale_return = pd.read_csv(whale_returns_path, index_col='Date', parse_dates=True, infer_datetime_format=True)
    whale_return = whale_return.dropna()
    whale_return.isnull().sum()
    algo_returns_path = Path("Resources/algo_returns.csv")
    algo_return.isnull().sum()
    algo_return = algo_return.dropna()
    algo_return.isnull().sum()
    sp500_returns_path = Path("Resources/sp500_history.csv")
    sp500_close_price.dtypes
    sp500_close_price["Close"] = sp500_close_price["Close"].str.replace("$", "")
    sp500_close_price = sp500_close_price.astype(float)
    sp500_close_price = sp500_close_price.sort_index(ascending=True)
    sp500_return = sp500_close_price.pct_change()
    sp500_return = sp500_return.dropna()
    sp500_return.isnull().sum()
    sp500_return = sp500_return.rename(columns={"Close":"SP500"})
    whale_algo_sp500_daily_return = pd.concat([whale_return, algo_return, sp500_return], axis="columns", join="inner")
    whale_algo_sp500_daily_return.plot(figsize=(20, 10), title="Daily Returns")


if __name__ == '__main__':
    main()
