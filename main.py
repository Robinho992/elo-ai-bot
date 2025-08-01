import telebot
import datetime

TOKEN = "8288547656:AAHw6b1q7MUEK9s3Rb7uotND5r7VMTgoJpI"
bot = telebot.TeleBot(TOKEN)

def get_elo_prediction():
    return "📊 Прогноз: Победа игрока A (ELO рейтинг выше)"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот прогнозов на футбол и теннис на основе ELO и AI.")

@bot.message_handler(commands=["prognoz"])
def send_prediction(message):
    prediction = get_elo_prediction()
    bot.send_message(message.chat.id, prediction)

bot.polling()
