class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary  #Protected attribute
        self.__ssn = ssn       #Private attribute

    #get private attribute into public function than get the value
    def show_ssn(self):
        print(f"Employee ssn: {self.__ssn}")

employee1 = Employee("anas", 50000, 1234)


print(f"Employee name: {employee1.name}")
print(f"Employee salary: {employee1._salary}")
employee1.show_ssn()


#it can be access using name-mangling(not recommended)
#print(employee1._Employee__ssn)