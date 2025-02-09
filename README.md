# 🚀 Crypto Alert Bot

## 📌 Introduction
Crypto Alert Bot is a Telegram-integrated tool that tracks real-time cryptocurrency price changes and sends alerts when significant fluctuations occur.

---

## 🌟 Features
- ✅ Real-time cryptocurrency price tracking 📊  
- ✅ Sends alerts to Telegram when prices fluctuate beyond a set threshold 📢  
- ✅ Runs as a `systemd` service for stability and automatic restarts 🔄  
- ✅ Easy to configure and update 🛠️  
- ✅ Secure and lightweight 🚀  

---

## 📥 Installation & Setup

### **1️⃣ Connect to Your Server**
Ensure you have SSH access to the server where you want to run the bot:
```sh
ssh azureuser@<server-ip>
```

### **2️⃣ Clone the Repository**
Download the bot's source code:
```sh
git clone https://github.com/your-username/crypto-alert-bot.git
cd crypto-alert-bot
```

### **3️⃣ Set Up Virtual Environment**
Create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **4️⃣ Configure the Bot**
Update `config.py` with your Telegram bot token and chat ID:
```python
TELEGRAM_BOT_TOKEN = "your-telegram-bot-token"
TELEGRAM_CHAT_ID = "your-chat-id"
```
⚠ **Security Warning:** Do NOT commit sensitive credentials to public repositories.

---

## ⚡ Running the Bot

### **1️⃣ Start the Bot Manually**
```sh
python3 crypto_alert_bot.py
```

### **2️⃣ Running via `systemd`**
Ensure the bot restarts automatically by running it as a `systemd` service:
```sh
sudo systemctl start crypto_alert_bot
```

### **3️⃣ Enable Auto-Start on Boot**
```sh
sudo systemctl enable crypto_alert_bot
```

---

## 🔧 Managing the Bot

### **Check Bot Status**
```sh
sudo systemctl status crypto_alert_bot
```

### **Stop the Bot**
```sh
sudo systemctl stop crypto_alert_bot
```

### **Restart the Bot**
```sh
sudo systemctl restart crypto_alert_bot
```

---

## 🔍 Debugging & Logs
If the bot is not functioning correctly, check its logs:
```sh
journalctl -u crypto_alert_bot --reverse -n 50
```
To see live logs:
```sh
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
💰 Current price: $43,500.12
```

---

## 🛠 Troubleshooting

🔴 **Bot is not sending messages?**  
- Check if the Telegram bot token is correct.
- Verify that the bot has permissions to send messages to the chat.

🔴 **Bot crashes on startup?**  
- Run `python3 crypto_alert_bot.py` manually to check for errors.
- Check logs with `journalctl -u crypto_alert_bot -n 50`.

🔴 **Service not found when using `systemctl`?**  
- Ensure the service file is correctly set up (`/etc/systemd/system/crypto_alert_bot.service`).
- Reload `systemd` configuration with:
  ```sh
  sudo systemctl daemon-reload
  ```

---

## 📦 Docker Support (Optional)
If you prefer running the bot using Docker:
```sh
docker build -t crypto-alert-bot .
docker run -d --name crypto-alert-bot crypto-alert-bot
```

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

---

## 📞 Contact
💬 Telegram: [@bartate](https://t.me/bartate)  
💻 Discord: `amoszigller`

---

🚀 **Enjoy seamless crypto tracking with Crypto Alert Bot!**

