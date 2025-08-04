import random

def check_winner(user, comp):
    if user == comp or (user[0] == comp[0] and len(user) == 1):
        print(f"It's a draw! Computer chose {comp}")
    elif (user in ["rock", "r"] and comp in ["scissors", "s"]) or \
         (user in ["paper", "p"] and comp in ["rock", "r"]) or \
         (user in ["scissors", "s"] and comp in ["paper", "p"]):
        print(f"You win! Computer chose {comp}")
    else:
        print(f"You lost! Computer chose {comp}")

options = ["rock", "paper", "scissors", "r", "p", "s"]

while True:
    user = input("\nEnter your choice (rock, paper, or scissors). Type 'q' to quit: ").lower()
    if user in ['q', 'quit']:
        print("Thanks for playing! 👋")
        break

    if user not in options:
        print("Invalid input! Please enter rock, paper, or scissors.")
    else:
        comp = random.choice(["rock", "paper", "scissors"])  # only full names for comp
        check_winner(user, comp)
