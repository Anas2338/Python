def print_multiple(message, repeat):
    stop = repeat + 1
    for i in range(1, stop):
        print(i, message)


def main():
    message = input("Please type a message: ")
    repeat = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeat)

main()