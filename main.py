import os
import telebot
import random

TOKEN = os.getenv("TOKEN_BOT")
ADMIN_ID = 927058267

bot = telebot.TeleBot(TOKEN)

good_responses = [
    "👑 سلام رئیس!",
    "🔥 در خدمتم!",
    "💎 سرور گروه اومد!",
]

funny_responses = [
    "😂 چی میگی تو؟",
    "رفیق اینو از کجا آوردی؟ 🤔",
    "نه دیگه اینو قبول ندارم 😄",
    "😂 خندم گرفت",
    "چی کشیدی؟ 😏",
  "چی میگی زبون بسته 😂", 
]

@bot.message_handler(func=lambda message: True)
def reply(message):
    user_id = message.from_user.id

    if user_id == ADMIN_ID:
        bot.reply_to(message, random.choice(good_responses))
    else:
        bot.reply_to(message, random.choice(funny_responses))

bot.infinity_polling(skip_pending=True)
