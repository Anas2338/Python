class Operations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def Add(self):
        return (self.num1 + self.num2)
    
    def Subtract(self):
        return (self.num1 - self.num2)
    
    def multiply(self):
        return(self.num1 * self.num2)
    
    def divide(self):
        if self.num2 == 0 :
            raise ValueError("Cannot divided by Zero")
        return (self.num1 / self.num2)
    
    def show_all(self):
        print(f"Addition: {self.Add()}")
        print(f"Subtraction: {self.Subtract()}")
        print(f"Multiplication: {self.multiply()}")
        print(f"Division: {self.divide()}")

