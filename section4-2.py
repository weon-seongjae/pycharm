# Syntax and Simple Inheritance Example

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

class Student(Person):

    def __init__(self, first, last, stunum):
        Person.__init__(self,first, last)
        self.stunum = stunum

    def GetStudent(self):
        return self.Name() + ", " +  self.stunum

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")
z = Student("Jini", "Simpson", "7777")

print(x.Name())
print(y.GetEmployee())
print(z.GetStudent())