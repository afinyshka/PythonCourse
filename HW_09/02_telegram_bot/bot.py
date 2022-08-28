import pafy
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from datetime import datetime
from os import getenv
from sys import exit

from random import randint

from keyboards import get_keyboard, whos_turn_keyboard, menu, back, make_keyboards
from xo_game import winning_positions, convert_user_data_to_plain_list
from utils import get_title, get_download_url_best_audio, get_url, get_download_url_best_video, get_download_url_with_audio, get_author
from weather import weather

bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)

# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
print('Bot is initialiezed...')

available_moves = ['1','2','3','4','5','6','7','8','9']
user_data = []

class MoveState(StatesGroup):
    waiting_for_move_x = State()
    waiting_for_move_o = State()

class MoveBotState(StatesGroup):
    waiting_for_turn = State()
    waiting_for_player_move = State()
    waiting_for_bot_move = State()
class WeatherState(StatesGroup):
    waiting_for_place = State()

class Info(StatesGroup):
    video = State()

@dp.message_handler(commands=['gamebot'])
async def star_gamebot(message: types.Message):
    await message.answer("Вы запустили игру Крестики-нолики! ")
    await message.answer('Выберите за кого хотите играть:  ', reply_markup=whos_turn_keyboard())
    await MoveBotState.waiting_for_turn.set()


@dp.message_handler(state=MoveBotState.waiting_for_turn)
async def user_turns(message: types.Message, state: FSMContext):
    if message.text not in ["X", "O"]:
        await message.answer("Пожалуйста используйте клавиатуру снизу.")
        return
    if message.text == "X": # первый ход игрока
        user_data = {}
        await message.answer("Вы играете за X. Ваш ход: ", reply_markup=get_keyboard(user_data))
        await MoveBotState.waiting_for_player_move.set()
    if message.text == "O": # первый ход бота
        user_data = {}
        bot_move = randint(1,9)
        move_x: list = user_data.get('move_x') or []
        move_x.append(int(bot_move))
        await state.update_data(move_x=move_x)
        user_data = await state.get_data()
        print(user_data, type(user_data))
        await message.answer("Вы играете за O. Ваш ход: ", reply_markup=get_keyboard(user_data))
        await MoveBotState.waiting_for_bot_move.set()
        return user_data
        # {'move_x': [2, 4, 8], 'move_o': [5, 7, 3]} <class 'dict'>

@dp.message_handler(state=MoveBotState.waiting_for_player_move)
async def user_move(message: types.Message, state: FSMContext):
    if message.text not in available_moves:
        await message.answer("Пожалуйста используйте клавиатуру снизу.")
        return
    user_data = await state.get_data()
    move_x: list = user_data.get('move_x') or []
    move_o: list = user_data.get('move_o') or []
    if int(message.text) in move_x + move_o:
        await message.answer("Ой, тут уже занято, выбери другую клеточку:")
        return
    move_x.append(int(message.text))
    await state.update_data(move_x=move_x)
    user_data = await state.get_data()
    print(move_x, type(move_x), move_o, type(move_o))
    print(len(user_data['move_x']))

    game_result = winning_positions(convert_user_data_to_plain_list(user_data))
    if game_result == 'X':
        await message.answer('Вы выиграли!', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    if game_result == 'O':
        await message.answer('Вы проиграли.', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    if game_result == 'draw':
        await message.answer('Ничья!', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return

    # await message.answer("Ваш ход: ", reply_markup=get_keyboard(user_data))
    if len(user_data['move_x']) < 5:
        bot_move = randint(1, 9)
        move_x: list = user_data.get('move_x') or []
        move_o: list = user_data.get('move_o') or []
        while bot_move in move_x + move_o:
            bot_move = randint(1, 9)
        print(user_data, type(user_data))
        move_o.append(int(bot_move))
        await state.update_data(move_o=move_o)
        user_data = await state.get_data()

    game_result = winning_positions(convert_user_data_to_plain_list(user_data))
    if game_result == 'X':
        await message.answer('Вы выиграли!', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    if game_result == 'O':
        await message.answer('Вы проиграли.', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    if game_result == 'draw':
        await message.answer('Ничья!', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return

    await message.answer("Ваш ход: ", reply_markup=get_keyboard(user_data))

@dp.message_handler(state=MoveBotState.waiting_for_bot_move)
async def bot_moves(message: types.Message, state: FSMContext):
    if message.text not in available_moves:
        await message.answer("Пожалуйста используйте клавиатуру снизу.")
        return
    user_data = await state.get_data()
    print("user_data1 ", user_data)
    move_x: list = user_data.get('move_x') or []
    move_o: list = user_data.get('move_o') or []
    if int(message.text) in move_x + move_o:
        await message.answer("Ой, тут уже занято, выбери другую клеточку:")
        return
    move_o.append(int(message.text))
    await state.update_data(move_o=move_o)
    user_data = await state.get_data()
    print(user_data, type(user_data))

    game_result = winning_positions(convert_user_data_to_plain_list(user_data))
    if game_result == 'X':
        await message.answer('Вы проиграли!', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    if game_result == 'O':
        await message.answer('Вы выиграли.', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    if game_result == 'draw':
        await message.answer('Ничья!', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return

    move_x: list = user_data.get('move_x') or []
    move_o: list = user_data.get('move_o') or []
    bot_move = randint(1, 9)
    while bot_move in move_x + move_o:
        bot_move = randint(1, 9)
    move_x.append(int(bot_move))
    await state.update_data(move_x=move_x)
    user_data = await state.get_data()
    print(user_data, type(user_data))

    await message.answer("Ваш ход: ", reply_markup=get_keyboard(user_data))

    game_result = winning_positions(convert_user_data_to_plain_list(user_data))
    if game_result == 'X':
        await message.answer('Вы проиграли.', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    if game_result == 'O':
        await message.answer('Вы выиграли!', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    if game_result == 'draw':
        await message.answer('Ничья!', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return

@dp.message_handler(commands=['game'])
async def star_game(message: types.Message):
    await message.answer("You initialized XO game! ")
    keyboard = get_keyboard()
    await message.answer('Choose the cell for "X":  ', reply_markup=keyboard)
    await MoveState.waiting_for_move_x.set()


@dp.message_handler(state=MoveState.waiting_for_move_x)
async def user_move_x(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_moves:
        await message.answer("Please use the bellow keyboard.")
        return
    user_data = await state.get_data()
    move_x: list = user_data.get('move_x') or []
    move_o: list = user_data.get('move_o') or []
    if int(message.text.lower()) in move_x + move_o:
        await message.answer("Ooops, occupied. Try another cell:")
        return
    move_x.append(int(message.text))
    await state.update_data(move_x=move_x)
    user_data = await state.get_data()

    print("message text: ", message.text)
    game_result = winning_positions(convert_user_data_to_plain_list(user_data))
    if game_result == 'X':
        await message.answer('X-s win! Game over.', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    if game_result == 'O':
        await message.answer('O-s win! Game over.', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    if game_result == 'draw':
        await message.answer('You ended the game in a draw!', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    keyboard = get_keyboard(user_data)
    await MoveState.waiting_for_move_o.set()
    await message.answer('Choose the cell for "O":  ', reply_markup=keyboard)

@dp.message_handler(state=MoveState.waiting_for_move_o)   
async def user_move_o(message: types.Message, state: FSMContext):
    # message.text = bot_move() # кривое включение бота с переопределением команды
    if message.text.lower() not in available_moves:
        await message.answer("Please use the bellow keyboard.")
        return
    user_data = await state.get_data()
    move_x: list = user_data.get('move_x') or [] # user_data это словарь, в словаре есть метод get, в который передается ключ, если в словаре есть такой, то возвращается значение, если нет то None
    move_o: list = user_data.get('move_o') or []
    if int(message.text.lower()) in move_x + move_o:
        await message.answer("Ooops, occupied. Try another cell:")
        return
    move_o.append(int(message.text))
    await state.update_data(move_o=move_o)
    user_data = await state.get_data()
    print("message text: ",message.text)
    print(user_data, type(user_data))

    game_result = winning_positions(convert_user_data_to_plain_list(user_data))
    if game_result == 'X':
        await message.answer('X-s win! Game over.', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    if game_result == 'O':
        await message.answer('O-s win! Game over.', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    if game_result == 'draw':
        await message.answer('You ended the game in a draw!', reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return
    keyboard = get_keyboard(user_data)
    await MoveState.waiting_for_move_x.set()
    await message.answer('Choose the cell for "X":  ', reply_markup=keyboard)


@dp.message_handler(commands="cancel", state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['weather'])
async def start_weather(message: types.Message):
    await message.answer("Введите название города ")
    await WeatherState.waiting_for_place.set()

@dp.message_handler(state=WeatherState.waiting_for_place)
async def get_place(message: types.Message, state: FSMContext):
    await message.answer(weather(message.text))
    await state.finish()
    return



# Создаем message_handler и объявляем там функцию ответа:
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"Привет, {message.from_user.first_name}!\nСмотри, что я уже умею:\n/time - показать текущее время\n/game - игра в крестики нолики для двух игроков\n/gamebot - игра в крестики нолики с ботом\n/weather - показать текущую погоду\n/youtube - скачать видео с youtube\n/cancel - отмена\n/help - подсказки") # ответ на конкретноое сооьщение

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("/cancel - отменяет игру в любое время\n/start - для возврата в главное меню")

@dp.message_handler(commands=['time'])
async def process_time_command(message: types.Message):
    dt = datetime.now()
    time = dt.time()
    # time.strftime('%H:%M:%S')
    await message.reply(time.strftime('%H:%M:%S')) # "%H:%M"

@dp.message_handler(commands=['youtube'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=' Привет, я помогу тебе скачать видео с YouTube.', reply_markup = menu())

@dp.message_handler(text="Скачать")
async def save_video(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=' Введи ссылку на видео: ', reply_markup=back())
    await Info.video.set()

@dp.message_handler(state=Info.video, content_types=types.ContentTypes.TEXT)
async def edit_name(message: types.Message, state: FSMContext):
    if message.text.lower() == 'отмена':
        await bot.send_message(chat_id=message.chat.id, text='Ты вернулся в главное меню.', reply_markup=menu())
        await state.finish()
    else:
        if message.text.startswith('https://www.youtube.com/watch?v='):
            try:
                video_url = message.text
                await bot.send_message(chat_id=message.chat.id, text=f'Название видео: {get_title(video_url)}\nАвтор: {get_author(video_url)}\n\nВыберите качество загрузки:', reply_markup = make_keyboards(video_url))
                await state.finish()
            except OSError:
                await bot.send_message(chat_id=message.chat.id, text=f'Ссылка неверная, либо видео не найдено. Введи ссылку в формате: ```https://www.youtube.com/watch?v=...```', reply_markup = back(), parse_mode="Markdown")
            except ValueError:
                await bot.send_message(chat_id=message.chat.id, text=f'Ссылка неверная, либо видео не найдено. Введи ссылку в формате: ```https://www.youtube.com/watch?v=...```', reply_markup = back(), parse_mode="Markdown")
        else:
            await bot.send_message(chat_id=message.chat.id, text=f'Введи ссылку в формате: ```https://www.youtube.com/watch?v=...```', reply_markup = back(), parse_mode="Markdown")


@dp.callback_query_handler()
async def handler_call(call: types.CallbackQuery, state: FSMContext):
    chat_id = call.from_user.id
    if call.data.startswith('best_with_audio'):
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        video_url = get_url(call.data)
        download_link = get_download_url_with_audio(video_url)
        await bot.send_message(chat_id=chat_id, text=f' Вот ваша ссылка на скачивание видео: {download_link}', reply_markup = menu())
    elif call.data.startswith('best_video'):
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        video_url = get_url(call.data)
        download_link = get_download_url_best_video(video_url)
        await bot.send_message(chat_id=chat_id, text=f' Вот ваша ссылка на скачивание видео: {download_link}', reply_markup = menu())
    elif call.data.startswith('best_audio'):
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        video_url = get_url(call.data)
        download_link = get_download_url_best_audio(video_url)
        await bot.send_message(chat_id=chat_id, text=f' Вот ваша ссылка на скачивание аудио: {download_link}', reply_markup = menu())
    elif call.data == 'cancel':
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await bot.send_message(chat_id=chat_id, text='Ты вернулся в главное меню.', reply_markup=menu())

# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text) # просто сообщение от бота

if __name__ == '__main__':
    executor.start_polling(dp)