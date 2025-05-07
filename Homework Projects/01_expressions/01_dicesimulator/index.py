import random

def roll_dice():
    die1:int = random.randint(1, 6)
    die2:int = random.randint(1, 6)
    total: int = die1+die2
    print(f"Total of two dice: {total}")


for i in range(3):
    print(f"Roll {i+1}:")
    roll_dice()