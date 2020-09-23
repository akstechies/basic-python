#file handling

import os

#f = open("myfile1.txt", "x")
f = open("myfile2.txt", "w")


f = open('testfile.txt', "r")
#print(f.read())
#print(f.read(5))     #returns first 5 chars
#print(f.readline())
print(f.readline())
f.close()

#for x in f:
#    print(x)

f = open('testfile.txt', "a")
f.write('Some more content')
f.close()

os.remove('testfile.txt')

