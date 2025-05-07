def main():
    first_number  = int(input("Please enter an integer to be divided: "))
    second_number = int(input("Please enter an integer to divide by: "))


    divide:int = first_number // second_number
    remainder:int = first_number % second_number

    print(f"The result of this division is {divide} with a remainder of {remainder}")


main()