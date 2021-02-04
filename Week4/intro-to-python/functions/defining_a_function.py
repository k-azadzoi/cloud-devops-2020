# Examples of defining functions in python

# What are functions?
# Functions are a collection of instructions

def nullary_function():  # nullary means that the function takes no arguments
    print("Hi Friends")


def get_user_info():
    user_info = []
    print("What is your name?")
    user_name = input()

    print("How old are you")
    user_age = input()

    user_info.append(user_name)
    user_info.append(user_age)

    print(user_info)


def parameter_function(first_person_name, second_person_name):
    print("Greetings " + first_person_name + " and " + second_person_name)


parameter_function("Spike", "Faye")


def add(x, y):
    total = x + y
    return total


print(add(5, 10))
