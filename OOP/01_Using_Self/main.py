class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student name: {self.name}")
        print(f"Student marks: {self.marks}")

Student1 = Student("Anas", 81)
Student1.display()

        