#   Practice to learn how to make classes in python

class Student:
    def __init__(self, student_id, name, address):
        #   init is a special method called the initializer
        #   self is always the first parameter because it gives access to the object's properties
        self.student_id = student_id
        self.name = name
        self.address = address


student_one = Student(1, "Keith Johnson", "Boston, MA")
print("id:{}, name:{}, address:{}".format(student_one.student_id, student_one.name, student_one.address))
# output is id:1, name:Keith Johnson, address: Boston, MA

print("The student's name is " + student_one.name)
print("The student's name is {}".format(student_one.name))
#   The output for both print statements is "The student's name is Keith Johnson"

student_one.email = "manbearpig@supercereal.com"
#   Creating a new attribute outside the original Student class
print("The student's email is " + student_one.email)
#   This will output "The student's email is manbearpig@supercereal.com"







