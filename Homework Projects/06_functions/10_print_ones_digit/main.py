def print_ones_digit(num):
    ans = num % 10
    print(ans)

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

main()