#json

import json

'''--------json to py -------------------'''

#json
x = '{"name": "Ayush", "age": 25, "city": "Lucknow"}'

#convert to py
y = json.loads(x)
print(y["name"])
print(y["age"])
print(y)

'''-----------------py to json ------------------'''

#dict

a = {
    'name': 'Abhinav',
    "age": 20,
    "city": "Mumbai"
}

#convert to json
y = json.dumps(x)

print(y)

print('------------------------------------')

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
















