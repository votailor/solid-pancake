from settings import TOKEN
from misc import get_word_definitions
import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN, parse_mode=None)


# handles basic commands and sends a greetings message
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello, I am a bot.\nYou can send me an English word and I will send you it's definition(s).")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    startbtn = types.KeyboardButton('/start')
    pingbtn = types.KeyboardButton('/ping')
    markup.add(startbtn, pingbtn)
    bot.send_message(message.chat.id, "Choose a command below or send me a word", reply_markup=markup)


# ping-pong, if sent via command using '/'
@bot.message_handler(commands=['ping'])
def send_welcome(message):
    bot.reply_to(message, "pong")


# if a single word is passed to a bot, replies with a list of definitions for it. does nothing otherwise
@bot.message_handler(func=lambda message: len(message.text.split()))  # func evaluates to True if len == 1 (1 == True)
def echo_all(message):
    definitions = get_word_definitions(message.text)
    if definitions is None:
        bot.reply_to(message, 'Please try again.')
    else:
        bot.reply_to(message, '• ' + '\n• '.join(definitions))

    # TODO: add more functionality
    #   or handle more cases


if __name__ == '__main__':
    bot.infinity_polling()
