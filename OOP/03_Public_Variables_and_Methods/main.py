class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return "car is starting"
    

car1 = Car("Toyota")

print(car1.brand)
print(car1.start())