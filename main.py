import telebot
from telebot import types

# توکن ربات خود را اینجا قرار دهید
BOT_TOKEN = "7685135237:AAEmsHktRw9cEqrHTkCoPZk-fBimK7TDjOo"

# آدرس سایت شما
WEBSITE_URL = "https://mbuiop.github.io/Giop/"

bot = telebot.TeleBot(BOT_TOKEN)

# دستور start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # ایجاد کیبورد inline
    markup = types.InlineKeyboardMarkup()
    play_button = types.InlineKeyboardButton("🎮 Play", url=WEBSITE_URL)
    markup.add(play_button)
    
    # پیام خوش‌آمدگویی
    welcome_text = """
🎮 خوش آمدید!

برای شروع بازی روی دکمه Play کلیک کنید.
    """
    
    bot.send_message(
        message.chat.id,
        welcome_text,
        reply_markup=markup
    )

# دستور play
@bot.message_handler(commands=['play'])
def send_play_button(message):
    # ایجاد کیبورد inline
    markup = types.InlineKeyboardMarkup()
    play_button = types.InlineKeyboardButton("🎮 Play", url=WEBSITE_URL)
    markup.add(play_button)
    
    bot.send_message(
        message.chat.id,
        "🎮 برای شروع بازی روی دکمه زیر کلیک کنید:",
        reply_markup=markup
    )

# پاسخ به پیام‌های متنی
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # ایجاد کیبورد inline
    markup = types.InlineKeyboardMarkup()
    play_button = types.InlineKeyboardButton("🎮 Play", url=WEBSITE_URL)
    markup.add(play_button)
    
    bot.send_message(
        message.chat.id,
        "🎮 برای شروع بازی روی دکمه Play کلیک کنید:",
        reply_markup=markup
    )

# راه‌اندازی ربات
if __name__ == "__main__":
    print("ربات شروع شد...")
    bot.infinity_polling()