MAXIMUM_HEIGHT = 18

def main():
    height = float(input("How tall are you? "))

    if height >= MAXIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

main()