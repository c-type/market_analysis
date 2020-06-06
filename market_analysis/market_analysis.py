import yfinance as yf
import matplotlib.pyplot as plt

with open('./data/default_tickers.txt') as ticker_file:
    tickers = [ticker.strip() for ticker in ticker_file.readlines()]



class Stock:
    def __init__(self, ticker_obj):
        self.stock = ticker_obj
        self.hist = self.stock.history(period="max")
        self.daily_volatility()
        
    def daily_volatility(self):
        self.hist['volatility'] = abs((self.hist.Low - self.hist.High) / self.hist.High)

stocks = {}
for ticker in tickers:
    stocks[ticker]=Stock(yf.Ticker(ticker))

