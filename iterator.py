#iterator

mytuple = ('apple', 'mango', 'grapes')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print()

mystr = "banana"
myitr = iter(mystr)

print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))

print('---------------------------------------------')

class MyNum:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNum()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print('---------------------------------------------')


















