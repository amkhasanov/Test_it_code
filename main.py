import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_sti = open('Sticker/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, welcome_sti)

    bot.send_message(message.chat.id, f"Приветствую тебя ученик Python-а! {message.from_user.username}",
                     parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    username = message.from_user.username
    msg = f"Здравствуй, {username}"
    bot.send_message(message.from_user.id, msg)


bot.polling()
