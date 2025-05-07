class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value
    

val1 = Multiplier(2)

print(callable(val1))

print(val1(10))