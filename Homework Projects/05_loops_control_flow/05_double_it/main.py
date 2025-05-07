MAXIMUM_VALUE = 100

def main():
    current_value = int(input("Please Enter the number under 100: "))

    while True:
        updated_value = current_value * 2
        
        if current_value > MAXIMUM_VALUE:
            break

        print(f"{current_value} doubled is {updated_value}")

        current_value = updated_value
main()