# 2. Создайте программу для игры с конфетами человек против человека.
    
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
#     друг после друга. Первый ход определяется жеребьёвкой. 
#     За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#     Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
    
#     a) Добавьте игру против бота
    
#     b) Подумайте как наделить бота "интеллектом"

import random
    

def candy_hunter (number: int = 2021, number_taken_candies: int = 28) -> str:
    whos_turn = True # player_1 turn
    player_1 = input('Enter name of the 1-st player: ')
    player_1 = player_1.upper()
    player_2 = input('Enter name of the 2-nd player: ')
    player_2 = player_2.upper()
    player_1_candies = 0
    player_2_candies = 0
    rules = input(f'Hello {player_1} and {player_2}! Do you want to read the rules? yes or no? ')
    if rules.lower() == 'yes':
        print(f'''\nНа столе лежит {number} конфет(а).
Играют два игрока делая ход. За один ход можно забрать не более чем {number_taken_candies} конфет.
Все конфеты оппонента достаются сделавшему последний ход.''')
    who_first = random.randint(1,2)
    if who_first == 1:
        print(f"""\n... Now let's shake the dice... and ...  player number 1 is {player_1}.
And, {player_2}, you will be player number 2! So let's go! """)
    else:
        whos_turn = False # player_2 turn
        print(f"""\n... Now let's shake the dice... and ...  player number 1 is {player_2}.
And, {player_1}, you will be player number 2! So let's go! """)
    while number > 0:
        print(f"You have got {number} candies on the table. Let's move on! ")
        if number < number_taken_candies:
            candy_remains = number
        else:
            candy_remains = number_taken_candies
        if whos_turn:
            take_candy = int(input(f'\n{player_1}, you can take from 1 to {candy_remains} candies. \nEnter your number: '))
            while (not 1 <= take_candy <= candy_remains):
                take_candy = int(input(f'''\nYou entered the wrong number. Try again.
{player_1}, you can take from 1 to {candy_remains} candies. \nEnter your number: '''))
            player_1_candies += take_candy
            whos_turn = False
        else:
            take_candy = int(input(f'\n{player_2}, you can take from 1 to {candy_remains} candies. \nEnter your number: '))
            while (not 1 <= take_candy <= candy_remains):
                take_candy = int(input(f'''\nYou entered the wrong number. Try again.
{player_2}, you can take from 1 to {candy_remains} candies. \nEnter your number: '''))
            player_2_candies += take_candy
            whos_turn = True
        number -= take_candy
    if whos_turn:
        print(f'''\nCongratulations! {player_2}, you are the winner! You took {player_2_candies} candies!
And according to yhe rules, {player_1}  will give you his(her) {player_1_candies} candies.\n''')
    else:
        print(f'''\nCongratulations! {player_1}, you are the winner! You took {player_1_candies} candies!
And according to the rules, {player_2}  will give you his(her) {player_2_candies} candies.\n''')

def candy_hunter_bot (number: int = 2021, number_taken_candies: int = 28) -> str:
    whos_turn = True # player_1 turn
    player_1 = input('Enter name of the 1-st player: ')
    player_1 = player_1.upper()
    player_2 = 'MR. BOT'
    player_1_candies = 0
    player_2_candies = 0
    rules = input(f'Hello {player_1}! I am {player_2}! Do you want to read the rules? yes or no? ')
    if rules.lower() == 'yes':
        print(f'''\nНа столе лежит {number} конфет(а).
Играют два игрока делая ход. За один ход можно забрать не более чем {number_taken_candies} конфет.
Все конфеты оппонента достаются сделавшему последний ход.''')
    who_first = random.randint(1,2)
    print(who_first)
    if who_first == 1:
        print(f"""\n... Now let's shake the dice... and ...  player number 1 is {player_1}.
And, {player_2}, you will be player number 2! So let's go! """)
    else:
        whos_turn = False # player_2 turn
        print(f"""\n... Now let's shake the dice... and ...  player number 1 is {player_2}.
And, {player_1}, you will be player number 2! So let's go! """)
    print(whos_turn)
    while number > 0:
        print(f"You have got {number} candies on the table. Let's move on! ")
        if number < number_taken_candies:
            candy_remains = number
        else:
            candy_remains = number_taken_candies
        if whos_turn:
            take_candy = int(input(f'\n{player_1}, you can take from 1 to {candy_remains} candies. \nEnter your number: '))
            while (not 1 <= take_candy <= candy_remains):
                take_candy = int(input(f'''\nYou entered the wrong number. Try again.
{player_1}, you can take from 1 to {candy_remains} candies. \nEnter your number: '''))
            player_1_candies += take_candy
            whos_turn = False
        else:
            take_candy = random.randint(1, candy_remains)
            print(f'''\n{player_2}, you can take from 1 to {candy_remains} candies.
{player_2} took {take_candy} candies''')
            player_2_candies += take_candy
            whos_turn = True
        number -= take_candy
    if whos_turn:
        print(f'''\nOh noo... {player_2} is the winner! He took {player_2_candies} candies!
And according to the rules, {player_1}, you will give him your {player_1_candies} candies.\n''')
    else:
        print(f'''\nCongratulations! {player_1}, you are the winner! You took {player_1_candies} candies!
And according to the rules, {player_2}  will give you his(her) {player_2_candies} candies.\n''')

def candy_hunter_intelligent_bot (number: int = 2021, number_taken_candies: int = 28) -> str:
    whos_turn = True # player_1 turn
    player_1 = input('Enter name of the 1-st player: ')
    player_1 = player_1.upper()
    player_2 = 'MR. BOT'
    player_1_candies = 0
    player_2_candies = 0
    rules = input(f'Hello {player_1}! I am {player_2}! Do you want to read the rules? yes or no? ')
    if rules.lower() == 'yes':
        print(f'''\nНа столе лежит {number} конфет(а).
Играют два игрока делая ход. За один ход можно забрать не более чем {number_taken_candies} конфет.
Все конфеты оппонента достаются сделавшему последний ход.''')
    who_first = random.randint(1,2)
    print(who_first)
    if who_first == 1:
        print(f"""\n... Now let's shake the dice... and ...  player number 1 is {player_1}.
And, {player_2}, you will be player number 2! So let's go! """)
    else:
        whos_turn = False # player_2 turn
        print(f"""\n... Now let's shake the dice... and ...  player number 1 is {player_2}.
And, {player_1}, you will be player number 2! So let's go! """)
    while number > 0:
        print(f"You have got {number} candies on the table. Let's move on! ")
        if number < number_taken_candies:
            candy_remains = number
        else:
            candy_remains = number_taken_candies
        if whos_turn:
            take_candy = int(input(f'\n{player_1}, you can take from 1 to {candy_remains} candies. \nEnter your number: '))
            while (not 1 <= take_candy <= candy_remains):
                take_candy = int(input(f'''\nYou entered the wrong number. Try again.
{player_1}, you can take from 1 to {candy_remains} candies. \nEnter your number: '''))
            player_1_candies += take_candy
            whos_turn = False
        else:
            if (number - number//(number_taken_candies + 1) * (number_taken_candies + 1) == 0) or number > number_taken_candies * 2 + 1:
                take_candy = random.randint(1, candy_remains)
            else:
                take_candy = number - number//(number_taken_candies + 1) * (number_taken_candies + 1)
            print(f'''\n{player_2}, you can take from 1 to {candy_remains} candies.
{player_2} took {take_candy} candies''')
            player_2_candies += take_candy
            whos_turn = True
        number -= take_candy
    if whos_turn:
        print(f'''\nOh noo... {player_2} is the winner! He took {player_2_candies} candies!
And according to the rules, {player_1}, you will give him your {player_1_candies} candies.\n''')
    else:
        print(f'''\nCongratulations! {player_1}, you are the winner! You took {player_1_candies} candies!
And according to the rules, {player_2}  will give you his(her) {player_2_candies} candies.\n''')

game_regime = int(input("""Choose the game regime:
1 - player 1 against player 2
2 - player 1 against Mr. Bot
3 - player 1 against intelligent Mr. Bot
Enter: \n """))
while (not 1 <= game_regime <= 3):
    game_regime = int(input("""You entered the wrong regime number. Try again. Enter a number from 1 to 3:
1 - player 1 against player 2
2 - player 1 against Mr. Bot
3 - player 1 against intelligent Mr. Bot:\n """))
if game_regime == 1:
    game = candy_hunter(1000, 200)
elif game_regime == 2:
    game = candy_hunter_bot(1000, 200)
elif game_regime == 3:
    game = candy_hunter_intelligent_bot(302, 19)