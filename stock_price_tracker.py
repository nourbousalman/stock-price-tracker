import yfinance as yf

def get_stock_price(stock_symbol):
    try:
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.history(period="1d")
        latest_price = stock_info['Close'].iloc[0]
        print(f"The latest closing price of {stock_symbol} is: ${latest_price:.2f}")
    except Exception as e:
        print(f"Error retrieving data for {stock_symbol}: {e}")

if __name__ == "__main__":
    stock_symbol = input("Enter the stock symbol (e.g., AAPL for Apple): ").upper()
    get_stock_price(stock_symbol)
