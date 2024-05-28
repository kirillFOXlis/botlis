from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard_1 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_1 = KeyboardButton ('Покажи взрослую лису')
    button_2 = KeyboardButton ('Перейти на следующую клавиатуру')
    keyboard_1.add( button_1, button_2)
    return keyboard_1

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_3 = KeyboardButton ('Покажи маленького лисёнка')
    button_4 = KeyboardButton ('Вернуться на предыдущую клавиатуру')
    keyboard_2.add( button_3, button_4)
    return keyboard_2