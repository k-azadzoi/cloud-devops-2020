# Write a function that takes two numbers as parameters
# Return a list of n smallest odd integers greater than or equal to start, in ascending order.

def get_even_integers(start, n):
    count = 0
    even_integer_list = []

    while count <= n - 1:
        if start % 2 == 0:  # check if start is an even number
            start += 2  # if it is add 2 to start and reassign value to start
            count += 1  # also increase the count by 1
            even_integer_list.append(start)  # append start into the even_integer_list
        elif start % 2 != 0:  # otherwise if start is an odd number
            start += 1  # add 1 to start and reassign value to start
            count += 1  # increase count by 1
            even_integer_list.append(start)  # append start into the even_integer_list
    return even_integer_list  # make sure to return


print(get_even_intergers(1, 10))
