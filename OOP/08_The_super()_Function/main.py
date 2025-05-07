class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the base class
        self.subject = subject

teacher = Teacher("Anas", "Accounts")

print(f"Teacher name: {teacher.name}, Subject: {teacher.subject}")