import random

def check_winner(user, comp):
    global win, draw, lost
    if user == comp or (user[0] == comp[0] and len(user) == 1):
        print(f"It's a draw! Computer chose {comp}\n")
        draw = True
        win = False
        lost = False

    elif (user in ["rock", "r"] and comp in ["scissors", "s"]) or \
         (user in ["paper", "p"] and comp in ["rock", "r"]) or \
         (user in ["scissors", "s"] and comp in ["paper", "p"]):
        print(f"You win! Computer chose {comp}\n")
        win = True
        draw = False
        lost = False

    else:
        print(f"You lost! Computer chose {comp}\n")
        lost = True
        win = False
        draw = False

options = ["rock", "paper", "scissors", "r", "p", "s"]
win_count = 0
lost_count = 0
draw_count = 0

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
        if (win == True):
            win_count += 1
            print("YOUR SCORE: ", win_count)
        elif(lost == True):
            lost_count += 1
        elif(draw == True):
            draw_count += 1
        
    print("WIN LOSS DRAW COUNTER: ")
    print("WINS: ", win_count)
    print("LOSS: ", lost_count)
    print("DRAW: ", draw_count)
    