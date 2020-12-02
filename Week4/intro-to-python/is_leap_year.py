year = 1992

if year % 4 == 0:
    # Have to convert int to a string in order to use within the print statement
    # Otherwise the error " unsupported operand type(s) for +: 'int' and 'str' "
    strYear = str(year)
    print(strYear + " is a leap year.")
else:
    print("No")