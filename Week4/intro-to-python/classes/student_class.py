#   Practice to learn how to make classes in python

class Student:
    def __init__(self, student_id, name, address):
        #   init is a special method called the initializer
        #   self is always the first parameter because it gives access to the object's properties
        self.student_id = student_id
        self.name = name
        self.address = address


student_one = Student(1, "Keith Johnson", "Boston, MA 01923")
print("id:{}, name:{}, address:{}".format(student_one.student_id, student_one.name, student_one.address))
# output is id:1, name:Keith Johnson, address: Boston, MA 01923
