# -*- coding: utf-8 -*-

"""
ربات تلگرام دانلودر اینستاگرام
نسخه نهایی و بهینه‌شده
توسعه داده شده برای نمونه‌کار

امکانات:
1. نصب خودکار وابستگی‌ها (python-telegram-bot، requests، beautifulsoup4)
2. پشتیبانی از دستور /start برای خوش‌آمد
3. پشتیبانی از دستور /insta و دریافت لینک اینستاگرام
4. دانلود مستقیم محتوا (در حال حاضر ساده شده برای نمونه‌کار)
5. سازگار با Railway و اجرا به صورت آنلاین

"""

import subprocess
import sys

# نصب خودکار کتابخانه‌ها در صورتی که نصب نشده باشند
def install_dependencies():
    try:
        import telegram
        import requests
        import bs4
    except ImportError:
        print("📦 نصب وابستگی‌ها...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 
                               "python-telegram-bot==13.15", 
                               "requests", 
                               "beautifulsoup4"])

install_dependencies()

# ایمپورت کتابخانه‌ها بعد از نصب
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
from bs4 import BeautifulSoup

# ---------------- تنظیمات ----------------
TOKEN = "8313464791:AAGRqM9KWeoJxjAYoTsey-Q3a-A50ajoZJk"

# ---------------- هندلر دستور /start ----------------
def start(update: Update, context: CallbackContext):
    """پیغام خوش‌آمد به کاربر"""
    update.message.reply_text(
        "👋 سلام! من ربات دانلودر اینستاگرام هستم.\n"
        "برای دانلود پست کافیست دستور زیر را وارد کنید:\n"
        "`/insta لینک_پست_اینستاگرام`",
        parse_mode=ParseMode.MARKDOWN
    )

# ---------------- هندلر دستور /insta ----------------
def insta(update: Update, context: CallbackContext):
    """
    دریافت لینک پست اینستاگرام و برگرداندن فایل یا تصویر
    در این نسخه نمونه‌کار، فقط لینک را بررسی و تایید می‌کند.
    """
    if len(context.args) == 0:
        update.message.reply_text("⚠️ لطفاً بعد از دستور /insta لینک اینستاگرام را وارد کنید.")
        return
    
    url = context.args[0]
    if not url.startswith("http"):
        update.message.reply_text("⚠️ لینک معتبر نیست. لطفاً لینک کامل را وارد کنید.")
        return

    try:
        # درخواست HTML
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        # پیدا کردن تگ‌های مربوط به تصویر یا ویدیو
        meta_tag = soup.find("meta", property="og:image")
        if meta_tag and meta_tag.get("content"):
            file_url = meta_tag["content"]
            update.message.reply_photo(photo=file_url, caption="✅ تصویر دانلود شد.")
        else:
            update.message.reply_text("❌ نتوانستم فایل را پیدا کنم یا این لینک عمومی نیست.")
    
    except Exception as e:
        update.message.reply_text(f"❌ خطا در پردازش لینک: {e}")

# ---------------- اجرای ربات ----------------
def main():
    """اجرای اصلی ربات"""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # ثبت دستورها
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("insta", insta))

    # شروع گوش دادن به پیام‌ها
    print("🚀 Bot started...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

# by Amir.T
