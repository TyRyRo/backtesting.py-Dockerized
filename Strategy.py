import pandas as pd
import talib
from backtesting import Strategy
from backtesting import Backtest
from backtesting.lib import crossover
from backtesting.test import GOOG

#Writing this for the BUY case only for now. Longs only, in an up market.
class ReversionDrive(Strategy):

    # Declare the moving average values to be used in the crossover/threshold condition.
    # Since these are **CLASS** values, they can be optimized later by the engine.
    moving_average_1 = 13
    moving_average_2 = 50
    RSI = 14

    def init(self):
        #Add logic to precompute indicator values inside init(). It should hold the entire series of values.
        self.ema1 = self.I(talib.EMA, self.data.Close, self.moving_average_1)
        self.ema2 = self.I(talib.EMA, self.data.Close, self.moving_average_2)
        self.rsi = self.I(talib.RSI, self.data.Close, self.RSI)
        

    def next(self):
        # This method is called iteratively, once for each row in the data frame.
        # Think of this as clicking the next button when manually backtesting.
        #if crossover(self.ema1, self.ema2):
            #self.position.close()
           # self.buy()
            if crossover(self.ema1, self.ema2) and self.rsi > 50:
                self.position.close()
                self.buy()

            elif crossover(self.ema2, self.ema1):
                self.position.close()
                self.sell()

bt = Backtest(GOOG, ReversionDrive, cash=1000, commission=0)
stats = bt.run()
print(stats)
#bt.plot()
