from utils.data_loader import fetch_stock_data
from backtester.backtest import run_backtest

def main():
    stock_symbol = input("Enter Stock Name: ")
    start_date = input("Enter Initial Date as YYYY-MM-DD: ")
    end_date = input("Enter Final Date as YYYY-MM-DD: ")
    
    print("Strategies: ")
    print("1. Moving Average")
    print("2. Percentage Change")
    strategy = input("Enter the number corresponding to the strategy you want to back test: ")
    # Fetch stock data
    df = fetch_stock_data(stock_symbol, start_date, end_date)
    
    # Run backtest
    final_value, profit_loss = run_backtest(df,strategy,stock_symbol)
    
    # Output results
    print(f"Final portfolio value: ${final_value:.2f}")
    print(f"Total profit/loss: ${profit_loss:.2f}")

if __name__ == "__main__":
    main()
