#regex

import re

txt = 'My name is Ayush'
x = re.search('^My.*Ayush$', txt)

print(x)

if (x):
    print('found')
else:
    print('absent')

y = re.findall('y', txt)
print(y)

z = re.search('\s', txt)    #returns white spaces
print(z)
print(z.start())

x = re.split("\s", txt)
print(x)

#x = re.sub("\s", "9", txt)  #without control
x = re.sub("\s", "10", txt, 2) #with control
print(x)