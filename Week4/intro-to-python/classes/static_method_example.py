#   Example of the class decorator - @staticmethod
# It does NOT take an implicit first argument
# Static methods are also bound to the class and not the object of the class.
# They do not have access to the state of the class.
# Can be called from an instance or a class object
# An example of its use is if we are using a class to group together related methods
# ..which don't need to access each other or any other data on the class.

from datetime import date


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Student object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


student1 = Student('Frank', 18)
student2 = Student('Regina', 15)

print(student1.age)
print(student2.age)

print(Student.isAdult(22))
# output is True
