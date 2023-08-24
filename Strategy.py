import pandas as pd
import talib
from backtesting import Backtest
from backtesting.lib import crossover, TrailingStrategy
from backtesting.test import GOOG

#Writing this for the BUY case only for now. Longs only, in an up market.
class MID_reversion(TrailingStrategy):

    # Declare the moving average values to be used in the crossover/threshold condition.
    # Since these are **CLASS** values, they can be optimized later by the engine.
    moving_average = 50
    midp_period = 14
    
    def init(self):
        super().init()
        #Add logic to precompute indicator values inside init(). It should hold the entire series of values.
        #My thought is that this is actually going through the entire dataframe and calculating another column for each row.
        self.midprice = self.I(talib.MIDPRICE, self.data.High, self.data.Low, self.midp_period)
        self.ema = self.I(talib.EMA, self.data.Close, self.moving_average)
        self.set_trailing_sl(1.5)
        
    def next(self):
        super().next()
        # This method is called iteratively, once for each row in the data frame.
        # Think of this as clicking the next button when manually backtesting.
        if ((self.data.Low <= self.midprice) and (self.data.Close >= self.midprice) and (self.midprice > self.ema)):
            self.position.close()
            self.buy()

bt = Backtest(GOOG, MID_reversion, cash=1000, commission=0)
stats = bt.run()
print(stats)
bt.plot()
