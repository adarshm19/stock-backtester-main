import yfinance as yf


def fetch_stock_data(symbol, start_date, end_date):
    stock = yf.download(symbol, start=start_date, end=end_date)
    stock.reset_index(inplace=True)
    stock['date'] = stock['Date']  # Rename column for consistency
    return stock[['date', 'Close']].rename(columns={'Close': 'close'})
