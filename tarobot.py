import random
import telebot 
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot (TOKEN)

cards = { "VI. Влюблённые 💑": "Карта говорит о жертвенной любви и поклонении. Один из партнёров слеп в своей влюблённости, другой принимает это как само собой разумеющееся. Оба видят не реального человека, а придуманный образ. Рано или поздно иллюзии разрушатся.",
    "XIX. Солнце ☀️": "Одна из самых тёплых карт. Человек испытывает к вам искренние, радостные, открытые чувства — без скрытых мотивов. Это взаимная радость и желание быть рядом на самом чистом уровне.",   
    "XV. Дьявол 😈": "Человек сильно увлечён вами физически — но за этим влечением стоит желание обладать или контролировать. Отношения притягательные но строятся на зависимости и манипуляции.",
    "XII. Наказание 🔗": "Человек чувствует что-то к вам, но его эмоции сопровождаются болью и ощущением тупика. Он завис в своих чувствах — не может ни вперёд ни назад."
}

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(telebot.types.KeyboardButton("💝 Вытащить карту"))

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,
    "Добро пожаловать в Таро Манара 🃏\n\nПредставь человека и нажми намкнопку, чтобы узнать о его чувствах к тебе.",
    reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "💝 Вытащить карту")
def otvet (message):
    card = random.choice (list(cards.keys()))
    predskazanie = cards [card]
    bot.reply_to(message, f"🃏{card}\n\n{predskazanie}")

bot.polling()