def phone_numbers():
    phonebook = {}

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_contacts(phonebook):
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")



def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} not in phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = phone_numbers()
    print_contacts(phonebook)
    lookup_numbers(phonebook)


main()

