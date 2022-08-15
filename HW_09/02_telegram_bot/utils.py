def convert_user_data_to_plain_list(user_data: dict[str, list]) -> list:
    """Конвертирует user_data в формат для функции winning_positions."""
    lst = [None, None, None, None, None, None, None, None, None]
    if not user_data.get('move_x') or not user_data.get('move_o'):
        return lst
    for i in user_data['move_x']:
        lst[i-1] = 'X'
    for i in user_data['move_o']:
        lst[i-1] = 'O'
    return lst