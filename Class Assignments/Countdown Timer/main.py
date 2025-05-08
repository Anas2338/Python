import time

second = int(input("Please enter time in seconds: "))

def countdown(second):
    while second > 0:
        print(f"Time left: {second}")
        time.sleep(1)
        second -= 1

    print("Time's Up!")


countdown(second)