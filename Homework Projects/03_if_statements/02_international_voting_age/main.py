EUROPE = 16
USA = 25
AUSTRALIA = 20


def main():

    user_age = int(input("How old are you? "))


    if user_age >= EUROPE:
        print(f"You can vote in Europe where the voting age is {EUROPE}")
    else:
        print(f"You cannot vote in Europe where the voting age is {EUROPE}")


    if user_age >= USA:
        print(f"You can vote in USA where the voting age is {USA}")
    else:
        print(f"You cannot vote in USA where the voting age is {USA}")


    if user_age >= AUSTRALIA:
        print(f"You can vote in Australia where the voting age is {AUSTRALIA}")
    else:
        print(f"You cannot vote in Australia where the voting age is {AUSTRALIA}")


main()