import random

MIN_VALUE=1
MAX_VALUE=100

def main():
    for i in range(10):
        numbers = random.randint(MIN_VALUE, MAX_VALUE)
        print(numbers)

    return(i)

main()