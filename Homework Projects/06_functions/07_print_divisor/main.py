def print_divisor(num):
    print(f"Here are the divisors of {num}")
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)



def main():
    num = int(input("Enter a number: "))
    print_divisor(num)


main()