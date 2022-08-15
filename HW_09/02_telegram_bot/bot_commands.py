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

move_storage = [1, 2, 5, 9]

move = (input("Enter the name of the sell meanings from 1 to 9 for {x}-mark: "))
while move in move_storage:
    move = (input("Warning! You entered wrong number. Enter the name of the sell meanings from 1 to 9 for {x}-mark: "))
print(move)
