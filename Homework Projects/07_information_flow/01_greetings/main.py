def greet(name):
    return "Greetings " + name + "!"

def main():
    name : str = input("What's your name? ")
    print(greet(name))


main()