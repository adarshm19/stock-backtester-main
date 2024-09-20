from strategies.moving_average import use_moving_average
from strategies.percentage_change import use_percentage_change_strategy

def run_backtest(df,strategy,stock_symbol):
    if strategy=="1":
        return use_moving_average(df,stock_symbol)
    if strategy=="2":
        return use_percentage_change_strategy(df,stock_symbol)

