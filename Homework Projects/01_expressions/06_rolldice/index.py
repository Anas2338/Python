import random

die_sides:int = 6

def main():
    die1:int = random.randint(1, die_sides)
    die2:int = random.randint(1, die_sides)

    total:int = die1 + die2

    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dies: {total}")

    

main() 