import random

def computer_guess():
    low = 1
    high = 10
    feedback = ""

    while feedback != "c":
        guess = random.randint(low, high)
        feedback = input(f"if {guess} too high(h), too low(l), or correct(c): ")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess} , correctly")


computer_guess()
