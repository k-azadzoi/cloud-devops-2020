# This is an example of one fo the class decorators the @classmethod
#

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    # The class argument is needed similar to the self argument
    # Class methods are bound to the class and not the object of the class.
    # Class methods are used to create factory methods which return a class objet for different use cases
    def from_fullname(cls, fullname):
        last_name, first_name = fullname.split(',')
        return cls(first_name, last_name)


student_one = Student.from_fullname('Jones, Mitch')
print("First Name: {}, Last Name: {}".format(student_one.first_name, student_one.last_name))
