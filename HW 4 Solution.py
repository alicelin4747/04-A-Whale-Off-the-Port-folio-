#inital imports
import pandas as pd
import numpy as np
import datetime as dt
from pathlib import Path

#%matplotlib inline

#set path to data file
whale_returns_path = Path("Resources/whale_returns.csv")
algo_returns_path = Path("Resources/algo_returns.csv")
sp500_returns_path = Path("Resources/sp500_history.csv")

whale_return_portfolio = pd.read_csv(whale_returns_path, index_col='Date', parse_dates=True, infer_datetime_format=True)
algo_return_portfolio = pd.read_csv(algo_returns_path, index_col='Date', parse_dates=True, infer_datetime_format=True)
sp500_return_portfolio = pd.read_csv(sp500_returns_path, index_col='Date', parse_dates=True, infer_datetime_format=True)

whale_return_portfolio.head()
algo_return_portfolio.head()
sp500_return_portfolio.head()




