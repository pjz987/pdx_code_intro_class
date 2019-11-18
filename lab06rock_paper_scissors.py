'''
filename: lab06rock_paper_scissors.py
Lab 6: Rock Paper Scissors
Let's play rock-paper-scissors with the computer.
'''

import random



'''
Advanced Version 1
Catch all tie conditions using a single if conditional
This doesn't really work so easily because I have a diffent string to print() for each tie... ##edit## I actually ended up figuring this out later.  See: lines 50-51
'''

'''
Advanced Version 2
Ask the user if they want to play again, using a while loop
'''
while True:
    # 1. The computer will ask the user for their choice (rock paper, scissors)

    user_choice = input("\nLet's play rock paper scissors!\n\nSo please choose Rock, Paper, or Scissors: ").lower()

    # 2. The computer will randomly choose rock, paper, or scissors

    r_p_s = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(r_p_s)
    print(f"\nYou chose {user_choice}. The computer chose {computer_choice}.\n")

    if user_choice == 'rock':
        if computer_choice == 'paper':
            print("Paper covers Rock.  The Computer wins.\n\nSorry.")
        if computer_choice == 'scissors':
            print("Rock breaks Scissors.  You win!\n\nCongratulations!")

    if user_choice == 'paper':
        if computer_choice == 'scissors':
            print("Scissors cut Paper.  The Computer wins.\n\nSorry...")
        if computer_choice == 'rock':
            print("Paper covers Rock.  You win!\n\nCongratulations!")

    if user_choice == 'scissors':
        if computer_choice == 'rock':
            print("Rock breaks Scissors.  The Computer wins.\n\nSorry...")
        if computer_choice == 'paper':
            print("Scissors cut Paper.  You win!\n\nCongratulations!")

    if user_choice == computer_choice:
        print(f"{user_choice} vs {computer_choice}.  It's a tie...")
#line 51 here ruins my rock, paper, scissors capitalizations.  I'll try to fix it... Couldn't really figure that out.  I'm sure I'll learn soon enough
    while True:
        play_again = input("\nWould you like to play again? ").lower()
        if play_again.lower() in ['yes', 'y', 'si', 'yea', 'yeah', 'sure', 'yes please']:
            break
        elif play_again.lower() in ['no', 'nope', 'no thanks', 'n', 'nein', 'nyet', 'non', 'nah']:
            break
        else:
            print("\nSorry, please answer again.")
    if play_again.lower() in ['no', 'nope', 'no thanks', 'n', 'nein', 'nyet', 'non', 'nah']:
        print("\nThanks for playing!")
        break

'''
line 55 was originially
    if play_again == 'no'
But I wanted to allow for other negative responses
I changed it to:
    if play_again.lower() in ['no', 'nope', 'no thanks']:
Using in [] will run the break on line 58 if play_again is in the list in the brackets
####All this comment info isn't totally applicable anymore because I changed the code so much####
'''
