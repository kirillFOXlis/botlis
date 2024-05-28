from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline_1():
    keyboard_inline1 = InlineKeyboardMarkup(row_width=2)
    bot_inline1 = InlineKeyboardButton('Посмотреть', url='https://roev.ru/posetitelyam/priroda/khishchnye/lisitsa_obyknovennaya.html')
    keyboard_inline1.add(bot_inline1)
    return keyboard_inline1

def get_keyboard_inline_2():
    keyboard_inline2 = InlineKeyboardMarkup(row_width=2)
    bot_inline2 = InlineKeyboardButton('Посмотреть',url='https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%8B%D0%BA%D0%BD%D0%BE%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F_%D0%BB%D0%B8%D1%81%D0%B8%D1%86%D0%B0')
    keyboard_inline2.add(bot_inline2)
    return keyboard_inline2

def get_keyboard_inline_3():
    keyboard_inline3 = InlineKeyboardMarkup(row_width=1)
    button11 = InlineKeyboardButton('Переключсь на клаву 1',callback_data='go2')
    keyboard_inline3.add(button11)
    return keyboard_inline3

def get_keyboard_inline_4():
    keyboard_inline4 = InlineKeyboardMarkup(row_width=1)
    button22 = InlineKeyboardButton('Переключись на клаву 2',callback_data='go1')
    keyboard_inline4.add(button22)
    return keyboard_inline4


def get_keyboard_inline_5():
    keyboard_inline5 = InlineKeyboardMarkup(row_width=1)
    button33 = InlineKeyboardButton('Переключсь на клаву 2',callback_data='go4')
    keyboard_inline5.add(button33)
    return keyboard_inline5

def get_keyboard_inline_6():
    keyboard_inline6 = InlineKeyboardMarkup(row_width=1)
    button44 = InlineKeyboardButton('Переключись на клаву 1',callback_data='go3')
    keyboard_inline6.add(button44)
    return keyboard_inline6
