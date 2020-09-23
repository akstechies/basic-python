#arrays

cars = ['bmw', 'lambo', 'dv avanti']

print(cars[1])
print(type(cars))

cars[0] = 'ferrari'
print(cars)

print(len(cars))

for x in cars:
    print(x)

print('-------------------------------')

#adding array elements

cars.append('bmw')
print(cars)

cars.pop()
print(cars)

cars.pop(0)
print(cars)

cars.remove('lambo')
print(cars)