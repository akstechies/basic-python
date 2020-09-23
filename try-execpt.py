#try-execpt

try:
    print(x)
except:
    print('Error! no x defined')

print('----------------------------')

try:
    print(z)
except NameError:
    print("That's a name error")
except:
    print('Kuck aur galti hogi')

print('----------------------------')

try:
    print(7)
except NameError:
    print("That's a name error")
else:
    print('saaf h sab')
    
print('----------------------------')

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

print('--------------------------------------')

a = -1

#if a < 0:
 #   raise Exception('a is greater than 0')

print('--------------------------------------')

b = 'Hello'

if not type(b) is int:
    raise TypeError('Only int allowed')

#

















