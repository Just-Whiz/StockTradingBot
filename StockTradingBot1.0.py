# Name: Christian Suy
# Program name: Stock Trading Bot

from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime

API_KEY = "PKRFBEWR0NTITQ3OIV19"
API_SECRET = "l1L4x9KbY7hRsJgOLPt8deCk1qcqCW8zsUhgGkg5"
BASE_URL = "https://paper-api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY": API_KEY,
    "API_SECRET": API_SECRET,
    "PAPER": True
}

# Life cycle methods
class MLTrader(Strategy):
    # Runs once (everytime the bot starts up)
    def initialize(self):
        pass
    # Runs on every tick (everytime new data is received)
    def on_trading_iteration(self):
        pass

start_date = datetime(2024,1,15)
end_date = datetime(2024,1)


broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name="mlstrat", broker=broker, parameters={})

strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={}
)