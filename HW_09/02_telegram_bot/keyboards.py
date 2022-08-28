from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup,\
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def whos_turn_keyboard():
    buttons = ['X','O']
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    return keyboard


def get_keyboard(user_data: dict[str, list] = None):
    buttons = ['1','2','3','4','5','6','7','8','9']
    if user_data:
        if user_data.get('move_x'):
            for i in user_data['move_x']:
                buttons[i-1] = 'X'
        if user_data.get('move_o'):
            for i in user_data['move_o']:
                buttons[i-1] = 'O'
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    return keyboard


def menu():
    download_button = KeyboardButton('Скачать')
    menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    menu_kb.add(download_button)
    return menu_kb

def back():
    button_back = KeyboardButton('Отмена')
    back_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    back_kb.add(button_back)
    return back_kb

def make_keyboards(url):
    inline_kb1 = InlineKeyboardMarkup()
    button = InlineKeyboardButton('Лучшее качество до 720p(с звуком).', callback_data=f'best_with_audio|{url}')
    button2 = InlineKeyboardButton('Лучшее качество(без звука).', callback_data=f'best_video|{url}')
    button3 = InlineKeyboardButton('Звук в лучшем качестве.', callback_data=f'best_audio|{url}')
    button4 = InlineKeyboardButton('Отмена', callback_data=f'cancel')
    inline_kb1.add(button)
    inline_kb1.add(button2)
    inline_kb1.add(button3)
    inline_kb1.add(button4)
    return inline_kb1
