# Crypto Alert Bot

![Crypto Alert Bot](https://your-image-url-here.com/logo.png)

## 📌 Introduction
This bot is designed to track cryptocurrency price changes and send alerts to Telegram when significant fluctuations occur.

---

## 🚀 Features
- Real-time cryptocurrency price tracking.
- Sends alerts to Telegram when prices fluctuate beyond a set threshold.
- Runs as a `systemd` service for stability and automatic restarts.
- Easy to configure and update.

---

## 📥 Installation & Setup

### **1️⃣ Connecting to the Server**
To use the bot, connect to the server where it is installed:
```bash
ssh azureuser@<server-ip>
```

### **2️⃣ Clone the Repository**
If you haven't already cloned the repository, run:
```bash
git clone https://github.com/your-username/crypto-alert-bot.git
cd crypto-alert-bot
```

### **3️⃣ Setting up Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **4️⃣ Configuring the Bot**
Update `config.py` with your Telegram bot token and chat ID:
```python
TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"
TELEGRAM_CHAT_ID = "your-chat-id"
```

---

## ⚡ Running the Bot

### **1️⃣ Start the bot manually**
```bash
python3 crypto_alert_bot.py
```

### **2️⃣ Running via `systemd`**
If installed as a `systemd` service:
```bash
sudo systemctl start crypto_alert_bot
```

### **3️⃣ Enable Auto-Start on Boot**
```bash
sudo systemctl enable crypto_alert_bot
```

---

## 🔧 Managing the Bot

### **Check Bot Status**
```bash
sudo systemctl status crypto_alert_bot
```

### **Stop the Bot**
```bash
sudo systemctl stop crypto_alert_bot
```

### **Restart the Bot**
```bash
sudo systemctl restart crypto_alert_bot
```

---

## 🔍 Debugging & Logs
If the bot is not functioning correctly, check its logs:
```bash
journalctl -u crypto_alert_bot --reverse -n 50
```
To see live logs:
```bash
journalctl -u crypto_alert_bot -f
```

---

## 📡 Telegram Alerts

### **Startup Message**
When the bot starts, it sends a message like:
```
✅ Bot is active! Tracking the following coins: BTC, ETH, SOL, ...
```

### **Price Change Alerts**
If a cryptocurrency price changes by more than 3%, the bot sends an alert:
```
⚠️ 📈 BTC price increased by 3.5% within 5 minutes!
💰 Current price: $43500.12
```

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📞 Contact
@bartate

