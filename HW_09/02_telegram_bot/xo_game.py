from random import randint

def matrix_text(list: list) -> str:
    str_text = list[0] + '  ' + list[1] + '  ' + list[2] + '\n' + list[3] + '  ' + \
        list[4] + '  ' + list[5] + '\n' + list[6] + \
        '  ' + list[7] + '  ' + list[8] + '\n'
    return (str_text)


def winning_positions(list: list):
    a = list[0]
    b = list[1]
    c = list[2]
    d = list[3]
    e = list[4]
    f = list[5]
    g = list[6]
    h = list[7]
    i = list[8]
    # win_list = [[a, b, c], [d, e, f], [g, h, i], [a, d, g], [b, e, h], [c, f, i], [a, e, i], [c, e, d]]
    if any((a == b == c == 'X', d == e == f == 'X', g == h == i == 'X', a == d == g == 'X', b == e == h == 'X', c == f == i == 'X', a == e == i == 'X', c == e == g == 'X')):
        return 'X'
    elif any((a == b == c == 'O', d == e == f == 'O', g == h == i == 'O', a == d == g == 'O', b == e == h == 'O', c == f == i == 'O', a == e == i == 'O', c == e == g == 'O')):
        return 'O'
    if all(list):
        return 'draw'
    else:
        return "game not over"

def bot_move ():
    move = str(randint(1,9))
    return move

# def get_move(move_storage, list_x_o):
#     while [int(move) for i in move_storage if move_storage.count(int(move)) > 0] or not move in ['1','2','3','4','5','6','7','8','9']:
#         move = int(move) - 1
#     return move