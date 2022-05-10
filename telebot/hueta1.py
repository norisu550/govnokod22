
import telebot
import re
import os
import subprocess


superuser = 0
username = 0 
bot = telebot.TeleBot('')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'SUPERUSER PC = 0 type passwd')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global superuser 
    global username
    S = message.text
    if S == "1488":
        superuser = 1
        username = message.chat.id
        bot.send_message(message.chat.id, 'superuser 1')
    if superuser == 1 and username == message.chat.id:
        rutn = subprocess.getoutput(S) 
        bot.send_message(message.chat.id, rutn)
        print("Выполнил эту хуйню:" + S)
    if  superuser != 1 or username != message.chat.id:
        bot.send_message(message.chat.id, 'superuser 0')
        print("Не выполнил эту хуйню:" + S)
bot.polling(none_stop=True, interval=0)

