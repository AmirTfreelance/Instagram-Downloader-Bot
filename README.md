# 📥 Telegram Instagram Downloader Bot

A simple yet effective **Telegram bot** for downloading Instagram post images directly into your Telegram chat.  
This project was developed as a **portfolio sample** to demonstrate Python development, Telegram Bot API integration, and deployment skills using free hosting platforms like [Railway](https://railway.app).

---

## ✨ Features
- **/start** command: Welcomes the user and explains how to use the bot.
- **/insta <link>** command: Extracts the image from a public Instagram post URL and sends it directly to the user.
- **Automatic dependency installation**: Installs required Python packages automatically in case they are missing.
- Optimized for **local** or **cloud deployment** (Railway, Replit, VPS, etc.).
- Fully commented code (Persian comments for demonstration purposes).
- Lightweight — ready to be used as part of a developer’s portfolio.

---

## 📂 Project Structure
bot.py # Main bot script

requirements.txt # Python dependencies

README.md # Project documentation

---

## 🛠 Requirements
The bot uses the following Python packages:

- [`python-telegram-bot==13.15`](https://github.com/python-telegram-bot/python-telegram-bot) — Telegram Bot API integration.
- [`requests`](https://docs.python-requests.org/) — HTTP requests.
- [`beautifulsoup4`](https://www.crummy.com/software/BeautifulSoup/) — HTML parsing.

These dependencies are listed in `requirements.txt` and will be installed automatically when running `bot.py`.

---

## 🚀 Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

2️⃣ Set your bot token

Open bot.py and replace:
TOKEN = "YOUR_BOT_TOKEN"
with your actual Telegram bot token (from BotFather).

3️⃣ Run locally

python bot.py
Once running, your bot will respond to /start and /insta commands in Telegram chat.

🌐 Deployment on Railway
This bot is designed for free hosting on Railway.app:
Create a GitHub repository containing this project.
Go to Railway → New Project → GitHub Repo → Select your repository.
Railway will install dependencies based on requirements.txt.
Add an Environment Variable in Railway:
Key: TOKEN
Value: <your-telegram-bot-token>
Deploy and enjoy your bot 24/7 without manual hosting.

⚡ Commands
(Command : Description)
/start :	Welcome message with usage instructions

/insta : <link>	Downloads the public Instagram post image and sends it to Telegram

📸 Example
User:
/insta https://www.instagram.com/p/xxxxxxxxx/

Bot:
(Sends the post’s image directly in chat)

📜 License
This project is licensed under the MIT License — you are free to use, modify, and distribute it with proper credit.

💡 Notes
This is a simplified downloader for portfolio demonstration; it works with public posts only.
For video downloads or private content, additional API integration and authentication methods are required.
Persian comments in the code are for instructional purposes and can be adapted based on your audience.

👨‍💻 Author
Amir.T — Python & Telegram Bot Developer
My GitHub: https://github.com/AmirTfreelance
