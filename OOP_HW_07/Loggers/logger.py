from datetime import datetime as dt
# from guid import dict_log


def get_log(res, oper):
    dtime = dt.now()
    with open('/Users/user/Desktop/GB/Python_Course/OOP_HW_07/Loggers/log.txt', 'a', encoding='utf-8') as file:
        file.write('{};\nоперация: {}; результат: {}\n'.format(dtime, oper, res))
