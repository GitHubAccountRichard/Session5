# Virtual dice game, you win if you roll a six, you lose  1 life you not
#you have three lives
from random import randint

lives = 3
while True: #sort of infinite loop
    dice_roll = randint(1, 6)
    if dice_roll == 6:

        print("You rolled a 6, you win!")
        break
    else:
        lives = lives - 1 #you lose a life
        print(f"You rolled a {dice_roll}, You lose a life, lives left {lives}")
    if lives == 0:
        print("You lost!")
        break
print("Thanks for playing!")