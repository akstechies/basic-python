#inheritance

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

x = Person('Ayush', "Srivastava")
x.printname()

class Student(Person):
    pass

x = Student("Abhinav", 'Srivastava')
x.printname()

print('----------------------------------------------')

class Teacher(Person):
    def __init__(self, fname, lname):
        #Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.graduationyear = 2019
        
a = Teacher('Anand', 'Kumar')
a.printname()
print(a.graduationyear)

class Parents(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.gradyear = year
        
    def welcome(self):
        print('Welcome ' + self.firstname,  " " + self.lastname + " grad year is " , self.gradyear)

b = Parents('Ayush', 'Anand', 1995)
print(b.gradyear)
b.welcome()





