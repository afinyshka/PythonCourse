from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from random import randint

from config import TOKEN
from xo_game import matrix_text, winning_positions, bot_move
from utils import convert_user_data_to_plain_list

bot = Bot(token=TOKEN)
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

def whos_turn_keyboard():
    buttons = ['X','O']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
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
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    return keyboard

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
    print(move_x, type(move_x), move_o, type(move_o))
    if int(message.text) in move_x + move_o:
        await message.answer("Ой, тут уже занято, выбери другую клеточку:")
        return
    # if user_data[move_o] == None:
    move_x.append(int(message.text))
    await state.update_data(move_x=move_x)
    user_data = await state.get_data()
 
    bot_move = randint(1,9)
    while bot_move in move_x + move_o:
        bot_move = randint(1,9)
    print(user_data, type(user_data))
    move_x: list = user_data.get('move_x') or []
    move_o: list = user_data.get('move_o') or []
    move_o.append(int(bot_move))
    await state.update_data(move_o=move_o)
    user_data = await state.get_data()

    await message.answer("Ваш ход: ", reply_markup=get_keyboard(user_data))

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

@dp.message_handler(state=MoveBotState.waiting_for_bot_move)
async def bot_moves(message: types.Message, state: FSMContext):
    if message.text not in available_moves:
        await message.answer("Пожалуйста используйте клавиатуру снизу.")
        return
    user_data = await state.get_data()
    print("user_data1 ",user_data)
    move_x: list = user_data.get('move_x') or []
    move_o: list = user_data.get('move_o') or []
    print(move_x, type(move_x), move_o, type(move_o))
    if int(message.text) in move_x + move_o:
        await message.answer("Ой, тут уже занято, выбери другую клеточку:")
        return
    # if user_data[move_o] == None:
    move_o.append(int(message.text))
    await state.update_data(move_o=move_o)
    user_data = await state.get_data()

    bot_move = randint(1,9)
    while bot_move in move_x + move_o:
        bot_move = randint(1,9)
    print(user_data, type(user_data))
    move_x: list = user_data.get('move_x') or []
    move_o: list = user_data.get('move_o') or []
    move_x.append(int(bot_move))
    await state.update_data(move_x=move_x)
    user_data = await state.get_data()

    await message.answer("Ваш ход: ", reply_markup=get_keyboard(user_data))

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


# Создаем message_handler и объявляем там функцию ответа:
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"Hello, {message.from_user.first_name}!\nSend me a text message /help for help!") # ответ на конкретноое сооьщение

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("/time - show current time\n/game - to start tic tac toe game\n/cancel - to cancel")

@dp.message_handler(commands=['time'])
async def process_time_command(message: types.Message):
    dt = datetime.now()
    time = dt.time()
    # time.strftime('%H:%M:%S')
    await message.reply(time.strftime('%H:%M:%S')) # "%H:%M"

# @dp.message_handler(commands=['matrix'])
# async def process_matrix_command(message: types.Message):
#     list_x_o = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
#     await message.answer(matrix_text(list_x_o)) # просто сообщение от бота

# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text) # просто сообщение от бота

if __name__ == '__main__':
    executor.start_polling(dp)