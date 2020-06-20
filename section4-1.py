# Overloading and Overriding

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname + " " + self.lastname


class Employee(Person):

    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum


class Student(Person):

    def __init__(self, first, last, stunum):
        super().__init__(first, last)
        self.stumnum = stunum


x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")
z = Student("Jini", "Simpson", "7777")
print(x)
print(y, y.staffnumber)
print(z, z.stumnum)

