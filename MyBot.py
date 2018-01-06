import telebot
token='513665410:AAEUwxNDV6q5Sg_29KwE0n2r9UoPH9Nm30I'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def commands(message):
	bot.send_message(message.chat.id,'Привет даун')
if __name__=='__main__':
	bot.polling(none_stop=True)
