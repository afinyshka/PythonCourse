# 3. Создайте программу для игры в "Крестики-нолики".

def matrix_print(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matrix]))

# for row in matrix:
#     for item in row:
#         ''.join('{:4}'.format(item))
#     print('\n')

def winning_positions (matrix: list):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]
    win_list = [[a, b, c], [d, e, f], [g, h, i], [a, d, g], [b, e, h], [c, f, i], [a, e, i], [c, e, d]]
    if (a == b == c == 'X' or d == e == f == 'X' or g == h == i == 'X' or a == d == g  == 'X' or b == e == h == 'X' or c == f == i == 'X'  or a == e == i == 'X' or c == e == g == 'X'):
        return 'X'
    elif (a == b == c == 'O' or d == e == f == 'O' or g == h == i == 'O' or a == d == g  == 'O' or b == e == h == 'O' or c == f == i == 'O'  or a == e == i == 'O' or c == e == g == 'O'):
        return 'O'
    else: return "draw"


def game_X_O (rows: int = 3, columns: int = 3):
    list_x_o = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    move_storage = []
    count = 0 # Number of players moves
    turn = True # X turn
    matrix_print(list_x_o)
    whos_turn = int(input('''Enter the number for players turns:
1 - player "X", player "O"
2 - player "O", player "O"
:'''))
    while not 1 <= whos_turn <= 2:
        whos_turn = int(input('''Warning! Enter the number for players turns:
1 - player "X", player "O"
2 - player "O", player "O"
:'''))
    if whos_turn == 2:
        turn = False
    while count < (rows * columns):
        if turn:
            move = input("Enter the name of the sell in format 'row' 'column', meanings from 1 to 3 for X: ")
            move = list(map(lambda x: int(x) - 1, move.split()))
            while [move for i in move_storage if move_storage.count(move) > 0] or not (0 <= move[0] <= 2 and 0 <= move[1] <= 2):
                move = input("Warning! You entered wrong number. Enter the name of the sell in format 'row' 'column', meanings from 1 to 3 for X: ")
                move = list(map(lambda x: int(x) - 1, move.split()))
            list_x_o[move[0]][move[1]] = "X"
            turn = False
        else:
            move = input("Enter the name of the sell in format 'row' 'column', meanings from 1 to 3 for O: ")
            move = list(map(lambda x: int(x) - 1, move.split()))
            if [move for i in move_storage if move_storage.count(move) > 0] or not (0 <= move[0] <= 2 and 0 <= move[1] <= 2):
                move = input("Warning! You entered wrong number. Enter the name of the sell in format 'row' 'column', meanings from 1 to 3 for O: ")
                move = list(map(lambda x: int(x) - 1, move.split()))
            list_x_o[move[0]][move[1]] = "O"
            turn = True
        move_storage.append(move)
        matrix_print(list_x_o)
        count += 1
        # here is win combination check:
        if (rows + columns - 2) < count < (rows * columns):
            if winning_positions(list_x_o) == 'X':
                print('   Hooray!!! X-s win!')
                break
            elif winning_positions(list_x_o) == 'O':
                print('   Hooray!!! O-s win!')
                break
        elif count == rows * columns:
            if winning_positions(list_x_o) == 'X':
                print('   Hooray!!! X-s win!')
            elif winning_positions(list_x_o) == 'O':
                print('   Hooray!!! O-s win!')
            else:
                print ('You ended the game in a draw!')
    print('The end!')
    return 


start = game_X_O()