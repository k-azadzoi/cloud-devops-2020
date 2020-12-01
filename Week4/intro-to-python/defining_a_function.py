# Examples of defining functions in python

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


def parameter_function(some_person_name):
    print("Greetings " + some_person_name)


def add(x, y):
    total = x + y
    return total


print(add(5, 10))

