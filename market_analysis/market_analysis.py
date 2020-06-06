import yfinance as yf
import matplotlib.pyplot as plt

with open('./data/tickers.txt') as ticker_file:
    tickers = [ticker.strip() for ticker in ticker_file.readlines()]



class Stock:
    def __init__(self, ticker_obj):
        self.stock = ticker_obj
        self.hist = self.stock.history(period="max")
        self.daily_volatility()
        
    def daily_volatility(self):
        self.hist['volatility'] = abs((self.hist.Low - self.hist.High) / self.hist.High)
        
    def plot_volatility(self):
        fig, ax = plt.subplots()
        self.hist['volatility'].plot(label='volatility')
        quant99 = self.hist['volatility'].quantile(0.999)
        ax.plot_date([self.hist.index.min(), self.hist.index.max()], [quant99, quant99],'-.', label=r'99.9% quantile $= {0:.3f}$'.format(quant99))
        std_value = self.hist['volatility'].std()
        ax.plot_date([self.hist.index.min(), self.hist.index.max()], [3*std_value, 3*std_value],'--', label=r'$3 \sigma = {0:.3f}$'.format(3*std_value))
        plt.title(self.stock.ticker + ' Volatility')
        plt.xlabel('Date')
        plt.legend()
        plt.show()

stocks = {}
for ticker in tickers:
    stocks[ticker]=Stock(yf.Ticker(ticker))

