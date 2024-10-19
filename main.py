import telebot

TOKEN = '7698335040:AAEvEwNeS00nH8TrolrAoTEvluMAtO3KCeg'
bot = telebot.TeleBot(TOKEN)

# Creamos los comandos ue necesitemos
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola soy un boy creado por MarlonDevs')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Puedo hablarte de lo que desees, siempre y cuando este dentro de las reglas, por ahora solo respondo a los comandos /start y /help')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    bot.polling(none_stop=True)