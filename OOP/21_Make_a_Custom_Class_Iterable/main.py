class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= 0:
            num = self.current
            self.current -= 1
            return num
        
        else:
            raise StopIteration
        

obj1 = Countdown(10)

for num in obj1:
    print(num)