import telebot
from telebot import types

token = '1319236024:AAGfjGwUcnyPY7elPaCvcLLZMOvXXT_pnWY'
bot = telebot.TeleBot(token)
# upd = bot.get_updates()


@bot.message_handler(commands=['start'])
def handle_command(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
        user_markup.row("/start")
        bot.send_message(message.chat.id, "HI!!!!", reply_markup=user_markup)
@bot.message_handler(content_types=['text'])
def handle_text(message):
        bot.send_message(message.chat.id, "Пока111")
    # if message.text == "Привет": #or message.text =="A" or message.text == "А"  or message.text == "а":
    #     bot.send_message(message.chat.id, "Пока")
    # elif message.text == "Пока":
    #     bot.send_message(message.chat.id, "Привет")
    # else:
    #     bot.send_message(message.chat.id, "lol")
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     if message.text == "Hi":
#         bot.send_message(message.chat.id, "how's it going?")
# bot.polling(none_stop=True, interval=0)
# @bot.message_handler(content_types=['text'])
# def handle handle_text(message)
#     if message.text == "И снова привет" or if message.text == 'Привет':
bot.polling(none_stop=True)
