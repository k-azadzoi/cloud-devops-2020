# A function that will print out if a year is a leap year or not.

def is_leap_year(year):
    str_year = str(year)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # Have to convert int to a string in order to use within the print statement
        # Otherwise the error " unsupported operand type(s) for +: 'int' and 'str' "
        return str_year + " is a leap year."
    else:
        return str_year + " is NOT a leap year."


print(is_leap_year(2012))
print(is_leap_year(2048))
print(is_leap_year(1992))
print(is_leap_year(2035))
