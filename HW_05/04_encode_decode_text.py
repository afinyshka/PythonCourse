# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.
# qqqrrrrggggvcv
# 3q4r4g1v1c1v

import os


def rle_encoding (text: str) -> str:
    text_encoded = ''
    count = 1
    for i in range (len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            if count > 1:
                text_encoded = text_encoded + str(count) + text[i]
            else:
                text_encoded = text_encoded + text[i]
            count = 1
    if count > 1:
        text_encoded = text_encoded + str(count) + text[i]
    else:
        text_encoded = text_encoded + text[i+1]
    return text_encoded

def rle_decoding (text: str) -> str:
    text_decoded = ''
    number = ''
    for i in range (len(text)):
        if text[i].isdigit():
            number += text[i]
        else:
            if not number == '':
                text_decoded = text_decoded + int(number) * text[i]
            else: 
                text_decoded = text_decoded + text[i]
            number = ''
    return text_decoded


path_1 = 'HW_05' + os.sep + '04_encode.txt'

with open (path_1, 'r') as data_1:
    text_str = data_1.readline()

text_encoded = rle_encoding(text_str) 
print('Text:         ',text_str)
print('Encoded text: ',text_encoded)

text_initial = rle_decoding(text_encoded)

path_2 = 'HW_05' + os.sep + '04_decode.txt'

with open (path_2, 'w') as data_2:
     data_2.write(text_initial)

print('Decoded text: ',text_initial)

# считала что если один символ, то его оставляем без единицы, так как единица доп символ, а тут вроде сжатие qqqrrrrggggvcv -> 3q4r4gvcv


