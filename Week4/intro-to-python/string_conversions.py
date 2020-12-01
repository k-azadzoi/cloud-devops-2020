# This file is about working with strings

some_string = "Python,Java"  # strings are immutable
some_string_lower_case = some_string.lower()  # assign to a new variable because of above comment
some_string_upper_case = some_string.upper()
print("I expect to see the words lower case")
print(some_string_lower_case)
print("I expect to see the words uppercase case")
print(some_string_upper_case)

print(some_string_upper_case[::-1])  # reversing a string
