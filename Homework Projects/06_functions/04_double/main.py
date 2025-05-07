def double(num:int):
    return num * 2


def main():
    num = int(input("Enter a number: "))

    double_num= double(num)

    print(f"Double that is {double_num}")


main()