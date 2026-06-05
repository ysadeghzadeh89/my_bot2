import os
import telebot
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("TOKEN_BOT")
bot = telebot.TeleBot(TOKEN)

def get_usd():
    try:
        r = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=IRR").json()
        return int(r["rates"]["IRR"])
    except:
        return None

def get_btc():
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice/USD.json").json()
        return int(float(r["bpi"]["USD"]["rate"].replace(",", "")))
    except:
        return None

def menu():
    m = InlineKeyboardMarkup()
    m.add(
        InlineKeyboardButton("💵 دلار", callback_data="usd"),
        InlineKeyboardButton("₿ بیت‌کوین", callback_data="btc")
    )
    return m

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 خوش اومدی\n\nیکی رو انتخاب کن:",
        reply_markup=menu()
    )

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "usd":
        price = get_usd()
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"💵 دلار: {price:,}")

    elif call.data == "btc":
        price = get_btc()
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, f"₿ بیت‌کوین: ${price:,}")

bot.infinity_polling(skip_pending=True)
