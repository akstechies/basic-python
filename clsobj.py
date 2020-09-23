#classes and objects

class MyClass:
    x = 5

cls = MyClass()
print(cls.x)

print()

class Name:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def urname(self):
        print("Your name is " + self.name)

c1 = Name("Ayush", 25)

print(c1.name)
print(c1.age)
c1.urname()

print('-----------------------------------------')

class Newclass:
    def __init__(kuchv, naam, umar):
        kuchv.naam = naam
        kuchv.umar = umar
    
    def newfun(khatra):
        print("Aapka naam hai " + khatra.naam)

c2 = Newclass('Vaibhav', 25)
print(c2.umar)
c2.newfun()

c2.umar = 24
print(c2.umar)

#del c2.umar
#print(c2.umar)

del c2
print(c2.naam)


#


















