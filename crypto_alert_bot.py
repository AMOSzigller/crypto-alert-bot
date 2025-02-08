import requests
import time
import asyncio
import telegram
from datetime import datetime

# הגדרת טוקן ו-ID של הקבוצה בטלגרם
TELEGRAM_BOT_TOKEN = "7702238069:AAEdTO6ks2-ikICgKo4JNv4dwqulvNpOgNY"
TELEGRAM_CHAT_ID = "-1002352550208"

# רשימת המטבעות למעקב
COINS = {
    "bitcoin": "btc",
    "ethereum": "eth",
    "solana": "sol",
    "edwin": "edwin",
    "tri-sigma": "tri-sigma",
    "griffain": "griffain"
}

# יצירת חיבור לבוט
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# פונקציה להבאת מחירים מ-CoinGecko
def get_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ",".join(COINS.keys()), "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    return response.json()

# שמירת מחירים ישנים
old_prices = get_prices()
time.sleep(300)  # מחכים 5 דקות להתחלה

async def send_alerts(alerts):
    if alerts:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="\n".join(alerts))

while True:
    print(f'⏳ בודק מחירים... {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    new_prices = get_prices()
    print('🔄 נתונים חדשים התקבלו:', new_prices)
    alerts = []
    
    for coin, symbol in COINS.items():
        old_price = old_prices.get(coin, {}).get("usd", 0)
        new_price = new_prices.get(coin, {}).get("usd", 0)
        
        if old_price > 0:
            change_percent = ((new_price - old_price) / old_price) * 100
            print(f"📊 {symbol.upper()}: מחיר ישן: {old_price}, מחיר חדש: {new_price}, שינוי: {change_percent:.2f}%")
            
            if abs(change_percent) >= 3:
                direction = "📈 עלייה" if change_percent > 0 else "📉 ירידה"
                if symbol in ['edwin', 'tri-sigma', 'griffain']:
                    alert_message = f"⚠️ {direction} של {change_percent:.2f}% במטבע {symbol.upper()} תוך 5 דקות!\n💰 מחיר נוכחי: {new_price:.4f}$"
                else:
                    alert_message = f"⚠️ {direction} של {change_percent:.2f}% במטבע {symbol.upper()} תוך 5 דקות!\n💰 מחיר נוכחי: {new_price:.2f}$"
                alerts.append(alert_message)
    
    if alerts:
        print('🚀 שולח התראה לטלגרם...')
    asyncio.run(send_alerts(alerts))
    old_prices = new_prices
    time.sleep(300)  # מחכים 5 דקות
