#Rule of rock,paper,scissor game = r > s, s > p, p > r

import random


def is_win(player1, player2):
    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or (player1 == 'p' and player2 == 'r'):
        return True
    
def play():
    user = input("What's your choice: 'r' for rock, 's' for scissor, 'p' for paper: ")
    computer = random.choice(['r', 's', 'p'])

    print(f"computer select: {computer}")

    if user == computer:
        return "It's tie"
    
    if is_win(user, computer):
        return "You won!"
    
    return "You lost"


print(play())