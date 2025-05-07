def main():
    fruits = {
        "apple" : 150,
        "mango" : 200,
        "banana" : 80,
        "watermelon" : 60,
        "cheeko" : 250,
        "shareefa" : 400,
        "strawberry" : 250,
    }


    total_cost = 0
    
    for fruit_name in fruits:
        price = fruits[fruit_name]
        quantity_selected = int(input(f"How many {fruit_name} do you want to buy?: "))
        total_cost += (price * quantity_selected)

    print(f"Your total is Rs {total_cost}")


if __name__ == '__main__':
    main()