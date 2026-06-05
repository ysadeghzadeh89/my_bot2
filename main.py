import os
import telebot
import random

TOKEN = os.getenv("TOKEN_BOT")
bot = telebot.TeleBot(TOKEN)

jokes = [
  "من اگه جای تو بودم این گوهو نمیخوردم 😂",
    "داداش اینو از کجا درآوردی؟ 🤔",
    "باز این الدنگ اومد 😂",
    "من قانع شدم تو نابغه‌ای 😎",
    "این کصشرت همیشه یادم میمونه 🤖",
    "یه کم استراحت کن 😄",
    "نشون دادی حتما یه کاره ای میشی 😂",
    "حرفتو شنیدم ولی دلیل نمیشه بفهمم 😐",
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "😂 ربات فان فعال شد! هرچی بگی جواب خنده‌دار میدم")

@bot.message_handler(func=lambda message: True)
def reply_fun(message):
    bot.reply_to(message, random.choice(jokes))

bot.infinity_polling(skip_pending=True)
