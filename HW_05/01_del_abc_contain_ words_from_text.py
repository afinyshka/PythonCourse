# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

def text_del (text_str:str, text_search:str) -> str:
    text_str = text_str.split()
    f = lambda x: not text_search in x
    new_lst = list(filter(f, text_str))
    return " ".join(new_lst)

text_given = 'абв читают все абвэшки на земле, абв-4-5 вышла кошка погулять, абв-шш хвостом вилять.'
text_find = 'абв'

new_text = text_del(text_given, text_find)
print('Text:',text_given)
print('Text new:',new_text)