import requests
import asyncio
import telegram
from datetime import datetime

# Define Telegram bot token and group chat ID
TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"
TELEGRAM_CHAT_ID = "your-chat-id"

# List of cryptocurrencies to track
COINS = {
    "bitcoin": "btc",
    "ethereum": "eth",
    "solana": "sol",
    "edwin": "edwin",
    "tri-sigma": "tri-sigma",
    "griffain": "griffain",
    "jupiter": "jup"
}

# Create a connection to the Telegram bot
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Function to fetch prices from CoinGecko
def get_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ",".join(COINS.keys()), "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    return response.json()

# 🛠️ Define a global variable in advance to prevent errors
old_prices = {}

# Function to send alerts to Telegram
async def send_alerts(alerts):
    if alerts:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="\n".join(alerts))

async def main_loop():
    global old_prices  # ✅ Prevents errors as old_prices is already defined

    # Fetch initial prices
    old_prices = get_prices()

    # Send a startup message listing tracked cryptocurrencies
    coins_list = ", ".join([symbol.upper() for symbol in COINS.values()])
    startup_message = f"✅ בוט פעיל! עוקב אחרי המטבעות: {coins_list}"
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=startup_message)

    while True:
        print(f'⏳ Checking prices... {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        new_prices = get_prices()
        print('🔄 New data received:', new_prices)
        alerts = []

        for coin, symbol in COINS.items():
            old_price = old_prices.get(coin, {}).get("usd", 0)
            new_price = new_prices.get(coin, {}).get("usd", 0)

            if old_price > 0:
                change_percent = ((new_price - old_price) / old_price) * 100
                print(f"📊 {symbol.upper()}: Old price: {old_price}, New price: {new_price}, Change: {change_percent:.2f}%")

                if abs(change_percent) >= 3:
                    direction = "📈 עלייה" if change_percent > 0 else "📉 ירידה"
                    alert_message = f"⚠️ {direction} של {change_percent:.2f}% במטבע {symbol.upper()} תוך 5 דקות!\n💰 מחיר נוכחי: {new_price:.4f}$" if symbol in ['edwin', 'tri-sigma', 'griffain', 'jupiter'] else f"⚠️ {direction} של {change_percent:.2f}% במטבע {symbol.upper()} תוך 5 דקות!\n💰 מחיר נוכחי: {new_price:.2f}$"
                    alerts.append(alert_message)

        if alerts:
            print('🚀 Sending alert to Telegram...')
            await send_alerts(alerts)

        old_prices = new_prices  # ✅ Update the variable after it is properly defined
        await asyncio.sleep(300)  # Wait for 5 minutes

# Start the main loop
asyncio.run(main_loop())
