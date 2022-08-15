from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import datetime

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from config import TOKEN
from xo_game import game_X_O

bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
print('Bot is initialiezed...')

available_moves = ['1','2','3','4','5','6','7','8','9']

class MoveState(StatesGroup):
    move = State()

@dp.message_handler(commands=['game'])
async def user_register(message: types.Message):
    await message.answer("You initialized XO game! ")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = available_moves
    keyboard.add(*buttons)
    await message.answer("Choose the cell:  ", reply_markup=keyboard)
    
    await MoveState.move.set()

# @dp.message_handler(commands=['move'])
# async def user_move(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = available_moves
#     keyboard.add(*buttons)
#     await message.answer("Choose the cell:  ", reply_markup=keyboard)
#     # await MoveState.move.set()


# Обратите внимание: есть второй аргумент
@dp.message_handler(state=MoveState.move)
async def move_chosen(message: types.Message, state: FSMContext):
    if message.text.lower() not in available_moves:
        await message.answer("Please, choose the button from the keybord low.")
        return
    print(message.text)
    await state.update_data(move=message.text.lower())
    await message.answer(f"Great! Your move is initialized... it's {message.text}", reply_markup=types.ReplyKeyboardRemove())
    await message.answer(text = game_X_O(message.text))
    return message.text



    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # for size in available_food_sizes:
    #     keyboard.add(size)
    # # Для последовательных шагов можно не указывать название состояния, обходясь next()
    # await OrderFood.next()
    # await message.answer("Теперь выберите размер порции:", reply_markup=keyboard)



# @dp.message_handler(state=MoveState.move)
# async def get_move(message: types.Message, state: FSMContext):
#     await state.update_data(move=message.text)
#     print(message.text)
#     await message.answer(f"Great! Your move is initialized...it's {message.text}", reply_markup=types.ReplyKeyboardRemove())
#     await message.answer(matrix_text(available_moves))






# Создаем message_handler и объявляем там функцию ответа:
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"Hello, {message.from_user.first_name}!\nSend me a text message!") # ответ на конкретноое сооьщение

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler(commands=['time'])
async def process_time_command(message: types.Message):
    dt = datetime.now()
    time = dt.time()
    # time.strftime('%H:%M:%S')
    await message.reply(time.strftime('%H:%M:%S')) # "%H:%M"

@dp.message_handler(commands=['matrix'])
async def process_matrix_command(message: types.Message):
    list_x_o = message.from_user.id
    # list_x_o = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    await message.reply(matrix_text(list_x_o)) # просто сообщение от бота

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text) # просто сообщение от бота

if __name__ == '__main__':
    executor.start_polling(dp)
    