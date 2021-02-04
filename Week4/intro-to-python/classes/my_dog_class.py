# A simple example of a class in python using instance methods.
from datetime import date


class Dog:
    # using instance attributes to define the dog class
    def __init__(self, breed, name, age, color, is_asleep=False):
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color
        self.is_asleep = is_asleep

    # creating instance methods that use self to reference the instance attributes
    def walk(self):
        return self.name + ' is walking!'

    def eat(self):
        return self.name + ' is eating!'

    # since I am changing the is_asleep attribute to True.
    # In the return statement I convert the is_alseep attribute to a string
    # That way it can be outputted to the console in the print statement
    def sleep(self):
        self.is_asleep = True
        return 'It is ' + str(self.is_asleep) + '. ' + self.name + ' is sleeping!'

    def wake_up(self):
        self.is_asleep = False
        return 'It is ' + str(self.is_asleep) + '. ' + self.name + ' is waking up!'

    @classmethod
    def from_birth_year(cls, breed, name, birth_year, color, is_asleep):
        today = date.today().year
        age = today - birth_year
        return cls(breed, name, age, color, is_asleep)


dog_one = Dog("Welsh Corgi", "Cyrus", "13", "brown", is_asleep=False)
dog_two = Dog("Golden Retriever", "Jordan", "5", "black", is_asleep=False)

print(dog_one.walk())
print(dog_two.eat())
print(dog_two.sleep())
print(dog_one.wake_up(), dog_one.eat())

dog_three = Dog.from_birth_year("Bulldog", "Cam", 2018, "dark brown", is_asleep=False)
print(dog_three.age)




