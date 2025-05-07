def main():
    numbers:list = [1, 2, 3, 4]

    for i in range(len(numbers)):
        elem_index = numbers[i]
        updated_number = elem_index * 2
        print(updated_number)


main()