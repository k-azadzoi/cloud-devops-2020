class Dog:

    def __init__(self, breed, name, age, color, is_asleep=False):
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color
        self.is_asleep = is_asleep

    def walk(self):
        return self.name + ' is walking!'

    def eat(self):
        return self.name + ' is eating!'

    def sleep(self):
        is_asleep = True
        return self.name + ' is sleeping!'


dog_one = Dog("Welsh Corgi", "Cyrus", "2", "brown", is_asleep=False)
dog_two = Dog("Golden Retriever", "Jordan", "4", "black", is_asleep=False)

print(dog_one.walk())
print(dog_two.eat())
print(dog_two.sleep())
print(dog_two.is_asleep)
