import random

print("WELCOME TO PASSWORD GENERATOR")

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number= "0123456789"
special_character = "!@#$%^&*()?"
all_character = lower_case + upper_case + number + special_character


quantity_of_password = int(input("How many passwords do you want to generate? "))
length_of_password = int(input("What should be the length of each password? "))

def password_generator(q, l):
    Passwords = []
    for i in range(q):
        password = [
            random.choice(lower_case),
            random.choice(upper_case),
            random.choice(number),
            random.choice(special_character)
        ]
        
        password += [random.choice(all_character) for _ in range(l - 4)]
        random.shuffle(password)
        Passwords.append("".join(password))

    for p in Passwords:
        print(p)


password_generator(quantity_of_password, length_of_password)