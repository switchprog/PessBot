import telebot

from telebot import types

from info import *

API_TOKEN = "6827940365:AAGgiiann7kq2ttnQ32b3M29yaDWsZBoalQ"

bot = telebot.TeleBot(API_TOKEN)

user_id = -1

data = {}

state = 0

menu = types.InlineKeyboardMarkup(row_width=2)
menu.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
         InlineKeyboardButton("No", callback_data="cb_no"))

keyboard = types.ReplyKeyboardMarkup(True)
button = types.KeyboardButton(text='Начало')
button1 = types.KeyboardButton(text='/help')
button2 = types.KeyboardButton(text='/restart')
keyboard.add(button, button1, button2)


@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = str(message.from_user.id)
    bot.send_message(message.chat.id, info_s['start'], reply_markup=keyboard)


@bot.message_handler(commands=['restart'])
def help_message(message):
    global data
    data = readFromJSON()
    keys = data.keys()
    if message.chat.id not in keys:
        saveNewToJSON(user_id)
    else:
        resetUserOnJSON(message.chat.id)
    bot.send_message(message.chat.id, info_s['restart'])
    bot.send_message(message.chat.id, info_s['start'], reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, info_s['help'])


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global state
    if call.data == "cb_yes":
        saveOldToJSON(call.from_user.id, state, "yes")
    elif call.data == "cb_no":
        saveOldToJSON(call.from_user.id, state, "no")

    if state == 1:
            bot.send_message(call.from_user.id, info_Q['q2'], reply_markup=menu)
            state = 2
    elif state == 2:
            bot.send_message(call.from_user.id, info_Q['q3'], reply_markup=menu)
            state = 3
    elif state == 3:
            bot.send_message(call.from_user.id, info_Q['q4'], reply_markup=menu)
            state = 4
    elif state == 4:
            bot.send_message(call.from_user.id, info_Q['q5'], reply_markup=menu)
            state = 5
    elif state == 5:
            count = 0
            bot.send_message(call.from_user.id, "Вы ответили на все вопросы, Ваш результат:")
            for temp in readFromJSON()[str(call.from_user.id)].values():
                if temp == "yes":
                    count += 1
            if count == 0:
                photo = open('1.jpg', 'rb')
                bot.send_photo(call.from_user.id, photo)
            elif count == 1:
                photo = open('2.jpg', 'rb')
                bot.send_photo(call.from_user.id, photo)
            elif count == 2:
                photo = open('3.jpg', 'rb')
                bot.send_photo(call.from_user.id, photo)
            elif count == 3:
                photo = open('4.jpg', 'rb')
                bot.send_photo(call.from_user.id, photo)
            elif count == 4:
                photo = open('5.png', 'rb')
                bot.send_photo(call.from_user.id, photo)
            elif count == 5:
                photo = open('6.jpg', 'rb')
                bot.send_photo(call.from_user.id, photo)


@bot.message_handler(content_types=['text'])
def textAnswer(message):
    global data
    global state
    data = readFromJSON()
    keys = data.keys()


    if message.text == "Начало":
        global state
        if user_id not in keys:
            saveNewToJSON(user_id)
            bot.send_message(message.chat.id, 'Ответьте на вопросы "Да" или "Нет".', reply_markup=types.ReplyKeyboardRemove())
            bot.send_message(message.chat.id, info_Q['q1'], reply_markup=menu)
            state = 1
        else:
            chooseQuestion(user_id)
    else:
        if user_id in keys:
            chooseQuestion(user_id)
        else:
            bot.send_message(message.chat.id, "Нажми /start или /help")


def chooseQuestion(usr_id):
    global state
    if data[usr_id]['question1'] == "":
        bot.send_message(usr_id, info_Q['q1'], reply_markup=menu)
        state = 1
    elif data[usr_id]['question2'] == "":
        bot.send_message(usr_id, info_Q['q2'], reply_markup=menu)
        state = 2
    elif data[usr_id]['question3'] == "":
        bot.send_message(usr_id, info_Q['q3'], reply_markup=menu)
        state = 3
    elif data[usr_id]['question4'] == "":
        bot.send_message(usr_id, info_Q['q4'], reply_markup=menu)
        state = 4
    elif data[usr_id]['question5'] == "":
        bot.send_message(usr_id, info_Q['q5'], reply_markup=menu)
        state = 5

bot.polling()