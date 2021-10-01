import telebot

# Create a bot with your token
bot = telebot.TeleBot("Type Your Telegram Bot Token Here")


# Command: /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Welcome to Telegram Auto Bot")


# Command: /help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "How can I help you?")


# For all the incoming messages, replying its length
@bot.message_handler()
def remaining_all(message):
    length = len(message.text)
    bot.reply_to(message, str(length))


# Status of the Connection
print("Telegram Bot Started ")
print("Press (ctrl+c) To Stop ")


# Start Replying
bot.infinity_polling()
