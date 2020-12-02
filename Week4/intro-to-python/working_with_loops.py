# Learning about loops in Python

# For loops

# Printing out each item in an array called shopping_list
shopping_list = ["apples", "milk", "bread"]

for item in shopping_list:
    print(item)

# Loop through an array of numbers
numbers = [20, 10, 7]
total = 0

for num in numbers:
    total = total + num

print(total)


# Looping through a range of numbers starting at 0 and ending at 4
for i in range(0, 5):  # this will print 0 1 2 3 4 on separate lines
    print(i)


for i in range(10, 0, -1):  # will countdown starting at 10 and ending at 1
    print(i)

i = 0
while i < 5:  # printing 0 1 2 3 4 using a while loop
    print(i)
    i += 1



