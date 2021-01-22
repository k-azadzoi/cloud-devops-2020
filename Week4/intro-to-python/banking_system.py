# Banking System

# Create a class named Bank and define the following properties
class Bank:
    # class attribute
    bank_name = "Bank of America"

    # __init__ method that takes value for branch_location and initializes it
    def __init__(self, branch_location):
        self.branch_location = branch_location

    @classmethod
    def change_bank(cls, new):
        cls.bank_name = new
        print('The bank name is:', new)

    def check_location(self):
        print("The current branch is " + self.branch_location)


b = Bank.bank_name
print(b)  # Output: "Bank of America"
Bank.change_bank('Salem Five')  # Output: "The bank name is: Salem Five"

s = Bank("Boston")
s.check_location()  # Output: "The current branch is Boston"
