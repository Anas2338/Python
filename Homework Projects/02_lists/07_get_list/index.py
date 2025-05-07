def main():
    lst=[]

    get_items= input("Enter a value: ")
    while get_items:
        lst.append(get_items)
        get_items= input("Enter a value: ")
    
    print("Here's the list: ", lst)


main()