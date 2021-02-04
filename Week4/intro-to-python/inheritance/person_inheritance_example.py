class Person:
    def intro(self):
        print("Hello, I am a person")

    def sleep(self):
        print("I am going to sleep")


class Student(Person):
    def intro(self):
        print("Hello, I am a student")


s = Student()
s.intro()  # Output: Hello, I am a student
s.sleep()  # Output: I am going to sleep

# The introduce method of Student class overrides the same method of Person class.
