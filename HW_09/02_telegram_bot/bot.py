from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from config import TOKEN
from xo_game import matrix_text, winning_positions
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
    if message.text.lower() not in available_moves:
        await message.answer("Please use the bellow keyboard.")
        return
    user_data = await state.get_data()
    move_x: list = user_data.get('move_x') or []
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