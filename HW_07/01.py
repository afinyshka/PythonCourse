from unicodedata import name
import json


# abonent = {'name': 'Maria', }

# print(type(abonent), abonent['name'])

# dictt = {'first_name': 'Maria', 'last_name': 'Aksenova', 'phone_number': '89261232323', 'comment': 'no'}
# for i in dictt.values():
#     print(dictt[i])
# for k in dictt.keys():
#     print(k)

data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}


with open('HW_07/01.json', 'r') as file:
    new_data: list = json.load(file)
    new_data = list(new_data)


with open('HW_07/01.json', 'w') as file:
    new_data.append(data)
    json.dump(new_data, file)

print(type(new_data))
print(new_data)
    
