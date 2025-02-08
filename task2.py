#Importing the dependencies
import yfinance as yf
import time
import random
import matplotlib.pyplot as plt
from plyer import notification  # For desktop alerts

#Art Banner
def print_banner():
    print("\n===================================")
    print(" 📈  STOCK PORTFOLIO TRACKER  📊 ")
    print("===================================\n")

# Fun messages for stocks
fun_messages = [
    "🚀 To the moon!",
    "📉 Oof... not looking good!",
    "💰 Keep holding, champ!",
    "🔥 Hot stock alert!",
    "📊 Diversification is key!",
    "😎 Smart investment!",
]

# Stock price thresholds for alerts
price_alerts = {
    "AAPL": 150,  # Alert if Apple goes below $150
    "TSLA": 200,  # Alert if Tesla goes below $200
    "MSFT": 280,  # Alert if Microsoft goes below $280
    "GOOGL": 2500,  # Alert if Google goes below $2500
}

# Your stock portfolio (Ticker Symbol -> Number of Shares)
portfolio = {
    "AAPL": 5,   # 5 shares of Apple
    "TSLA": 2,   # 2 shares of Tesla
    "MSFT": 3,   # 3 shares of Microsoft
    "GOOGL": 1,  # 1 share of Google
}

# Function to send desktop notifications
def send_alert(stock, price, threshold):
    notification_title = f"⚠️ Stock Alert: {stock} Dropped!"
    notification_message = f"{stock} is now at ${price:.2f}, below the alert threshold of ${threshold}!"
    
    notification.notify(
        title=notification_title,
        message=notification_message,
        app_name="Stock Tracker",
        timeout=5  # Notification will disappear after 5 seconds
    )

    print(f"🚨 ALERT: {stock} dropped below ${threshold}! Current Price: ${price:.2f}")

# Function to fetch stock prices
def get_stock_prices(portfolio):
    print_banner()
    print("Fetching live stock prices... ⏳\n")
    time.sleep(1)  # Just to make it feel real

    total_value = 0
    stock_values = {}

    for stock, quantity in portfolio.items():
        stock_info = yf.Ticker(stock)
        price = stock_info.history(period="1d")['Close'].iloc[-1]  # Latest price
        value = price * quantity
        total_value += value
        stock_values[stock] = value

        # Check for price drop alert
        if stock in price_alerts and price < price_alerts[stock]:
            send_alert(stock, price, price_alerts[stock])

        # Random fun message
        message = random.choice(fun_messages)

        print(f"📌 {stock}: ${price:.2f} x {quantity} = ${value:.2f} {message}")
        time.sleep(0.5)  # Small delay for effect

    print("\n===============================")
    print(f"💰 TOTAL PORTFOLIO VALUE: ${total_value:.2f} 💰")
    print("===============================\n")

    visualize_portfolio(stock_values)

# Function to visualize portfolio as a pie chart
def visualize_portfolio(stock_values):
    labels = stock_values.keys()
    values = stock_values.values()

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"])
    plt.title("Stock Portfolio Distribution 📊")
    plt.show()

# Run the tracker
get_stock_prices(portfolio)