# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# import datetime
# # from spy import *


# def hello(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(f'Hello {update.effective_user.first_name}')

# updater = Updater('5537724872:AAGVO_fuaOzv0naW9ehbmJ4VgfrUTRvgdlY')

# updater.dispatcher.add_handler(CommandHandler('hello', hello))

# print('server start')



# updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
# updater.dispatcher.add_handler(CommandHandler('time', time_command))
# updater.dispatcher.add_handler(CommandHandler('help', help_command))
# updater.dispatcher.add_handler(CommandHandler('sum', sum_command))

# updater.start_polling()
# updater.idle()


# def hi_command(update: Update, context: CallbackContext):
#     # log(update, context)
#     update.message.reply_text(f'Hi {update.effective_user.first_name}!')

# def help_command(update: Update, context: CallbackContext):
#     # log(update, context)
#     update.message.reply_text(f'/hi\\n/time\\n/help')

# def time_command(update: Update, context: CallbackContext):
#     # log(update, context)
#     update.message.reply_text(f'{datetime.datetime.now().time()}')

# def sum_command(update: Update, context: CallbackContext):
#     # log(update, context)
#     msg = update.message.text
#     print(msg)
#     items = msg.split() # /sum 123 534543
#     x = int(items[1])
#     y = int(items[2])
#     update.message.reply_text(f'{x} + {y} = {x+y}')

# move_storage = [1, 2, 5, 9]

# move = (input("Enter the name of the sell meanings from 1 to 9 for {x}-mark: "))
# while move in move_storage:
#     move = (input("Warning! You entered wrong number. Enter the name of the sell meanings from 1 to 9 for {x}-mark: "))
# print(move)

def matrix_print(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))

def matrix_text(list: list) -> str:
    str_text = list[0] + '  ' + list[1] + '  ' + list[2] + '\n' + list[3] + '  ' + list[4] + '  ' + list[5] + '\n' + list[6] + '  ' + list[7] + '  ' + list[8] + '\n'
    return (str_text)
      
      
# for row in matrix:
#     for item in row:
#         ''.join('{:4}'.format(item))
#     print('\n')

def winning_positions (list: list):
    a = list[0]
    b = list[1]
    c = list[2]
    d = list[3]
    e = list[4]
    f = list[5]
    g = list[6]
    h = list[7]
    i = list[8]
    win_list = [[a, b, c], [d, e, f], [g, h, i], [a, d, g], [b, e, h], [c, f, i], [a, e, i], [c, e, d]]
    if (a == b == c == 'X' or d == e == f == 'X' or g == h == i == 'X' or a == d == g  == 'X' or b == e == h == 'X' or c == f == i == 'X'  or a == e == i == 'X' or c == e == g == 'X'):
        return 'X'
    elif (a == b == c == 'O' or d == e == f == 'O' or g == h == i == 'O' or a == d == g  == 'O' or b == e == h == 'O' or c == f == i == 'O'  or a == e == i == 'O' or c == e == g == 'O'):
        return 'O'
    if all(list):
        return 'draw'
    else:
        return "game not over"

def get_move(x, mover, move_storage, list_x_o):
    move = mover
    while [int(move) for i in move_storage if move_storage.count(int(move)) > 0] or not move in ['1','2','3','4','5','6','7','8','9']:
        move = mover
    move = int(move) - 1
    list_x_o[move] = x
    print('move:',move)
    return move

def win_combination_check(list_x_o: list, rows: int = 3, columns: int = 3):
    if winning_positions(list_x_o) == 'X':
        print('   Hooray!!! X-s win!')
        return 'win'
    elif winning_positions(list_x_o) == 'O':
        print('   Hooray!!! O-s win!')
        return 'win'


def game_X_O (mover, rows: int = 3, columns: int = 3):
    print("You started the xo game")
    list_x_o = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    move_storage = []
    count = 0 # Number of players moves
    matrix_text(list_x_o)
    while count < (rows * columns):
        if count%2==0:
            move = get_move("X", mover, move_storage, list_x_o)
        else:
            move = get_move("O", mover, move_storage, list_x_o)
        move_storage.append(move+1)
        print(move_storage)
        print(matrix_text(list_x_o))
        count += 1
        if count > (rows + columns - 2) and (win_combination_check(list_x_o) == 'win'):
            break
        if count == 9:
            print ('You ended the game in a draw!')
    print('The end!')
    return matrix_text(list_x_o)


if __name__ == '__main__':
    start = game_X_O()