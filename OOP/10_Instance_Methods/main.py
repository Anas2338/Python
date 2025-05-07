class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"my pet name is {self.name} and his breed is {self.breed} & says Woof")
    

dog = Dog("Tommy", "German sheffard")

dog.bark()