class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Animal sound"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, species="Dog")

    def make_sound(self):
        return "Bark!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, species="Cat")

    def make_sound(self):
        return "Meow!"

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, species="Lion")

    def make_sound(self):
        return "Roar!"

def animal_sound(animal:Animal):
    print(f"{animal.name} the {animal.species} says: {animal.make_sound()}")