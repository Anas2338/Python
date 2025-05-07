class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = new_price

    @price.deleter
    def price(self):
        print("Deleting...")
        del self._price


p1 = Product("1050")
p2 = Product("2500")

print(f"Before change the price of p1: {p1.price}")
print(f"Before change the price of p2: {p2.price}")

p1.price = "1300"
p2.price = "3000"

print(f"After change the price of p1: {p1.price}")
print(f"After change the price of p2: {p2.price}")

del p1.price

#print{p1.price} # ❌ Error! (AttributeError: 'Person' has no attribute '_name')