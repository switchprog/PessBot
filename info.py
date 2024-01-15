import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

info_s = {
    'start': '''Здравствуйте! Я бот-анкета "Насколько ты пессимист?",
с моей помощью Вы можете узнать уровень Вашего пессимизма. Чтобы начать, нажмите на кнопку "Начало". 
Чтобы ознакомиться с доступными командами, нажмите "/help". ''',
    'help': '''Этот бот поможет Вам определить степень Вашего пессимизма.
Список доступных команд: 
/help - справочная информация по использованию бота.
/start - запуск бота.
/restart - перезапуск бота.
Начало - запуск тестирования.
На каждый вопрос Вам предложено ответить "Да" или "Нет".
В конце Вы получите изображение с результатами тестирования.''',
    'restart': '''Бот перезапущен.'''
}

info_u = {}

info_Q = {
    'q1': 'Когда вы задумываетесь о будущем, вы представляете как много вы сделаете и добьётесь?',
    'q2': 'В Вашем настроении преобладает радость?',
    'q3': 'Когда Вы собираетесь в новое место или идёте гулять с новой для Вас компанией, Вы предполагаете, что всё пройдёт успешно?',
    'q4': 'Вы не считаете себя пессимистом?',
    'q5': 'В детстве Вы рисовали солнышко посередине листа?'
}

def saveNewToJSON(usr_id):
    template = {
        "question1": "",
        "question2": "",
        "question3": "",
        "question4": "",
        "question5": ""
    }

    with open('user_db.json') as f:
        data = json.load(f)

    with open('user_db.json', 'w') as to:
        data[usr_id] = template
        json.dump(data, to)


def resetUserOnJSON(usr_id):
    template = {
        "question1": "",
        "question2": "",
        "question3": "",
        "question4": "",
        "question5": ""
    }

    with open('user_db.json') as f:
        data = json.load(f)

    data[usr_id] = template

    with open('user_db.json', 'w') as to:
        json.dump(data, to)

def saveOldToJSON(usr_id_int , position, msg):
    data = {}
    with open('user_db.json') as f:
        data = json.load(f)
    usr_id = str(usr_id_int)
    if position == 1:
        data[usr_id]["question1"] = msg
    elif position == 2:
        data[usr_id]["question2"] = msg
    elif position == 3:
        data[usr_id]["question3"] = msg
    elif position == 4:
        data[usr_id]["question4"] = msg
    else:
        data[usr_id]["question5"] = msg
    with open('user_db.json', 'w') as to:
        json.dump(data, to)

def readFromJSON():
    with open('user_db.json') as f:
        data = json.load(f)
    return data

