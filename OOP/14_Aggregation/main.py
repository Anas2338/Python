class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, employees):
        self.employees = employees  # Department does not own Employees

employee1 = Employee("Ahmed")
employee2 = Employee("Ali")


department = Department([employee1, employee2])

print(f"Department: {department}")

del department

print(f"emloyee1: {employee1}")
print(f"emloyee2: {employee2}")
