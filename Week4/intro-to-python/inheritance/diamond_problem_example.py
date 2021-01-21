# More examples of inheritance in Python


# base class
class Creature:
    def intro(self):
        print("Hello I am a creature")


# first child class
class Person(Creature):
    def intro(self):
        print("Hello I am a person")
        super().intro()


# second child class
class Fish(Creature):
    def intro(self):
        print("Hello I am a fish")
        super().intro()


# "grandchild" class
class Mermaid(Person, Fish):
    def intro(self):
        print("Hello I am a mermaid")
        super().intro()


m = Mermaid()
m.intro()

# Output:
# Hello I am a mermaid
# Hello I am a person
# Hello I am a fish
# Hello I am a creature

