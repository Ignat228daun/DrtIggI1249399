import telebot,requests
token='495640848:AAEUjkKbBOXVJlOZGlmdqhFRrQfmSmVfdMw'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def commands(message):
	bot.send_message(message.chat.id,'Привет даун')

