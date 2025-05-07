def num_in_stock(fruit):
    if fruit == "apple":
        return 250
    if fruit == "watermelon":
        return 200
    if fruit == "strawberry":
        return 500
    else:
        return 0
    

def main():
	fruit : str = input("Enter a fruit: ")
	stock = num_in_stock(fruit)
	if stock == 0:
		print("This fruit is not in stock.")
	else:
		print("This fruit is in stock! Here is how many:")
		print(stock)
            
main()