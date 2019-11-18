'''
filename : lab08guess_num.py
Lab 8: Guess the Number
Let's play 'Guess the Number', the computer will choose a random int between 1 and 10.  The user will then try to guess the number, and the program will tell them whether they're right or wrong.
'''

import random
comp_num = random.randint(1,10)
print("\nDo you have the gift?  Can you guess what the computer is thinking?\n\nCan you guess the correct number between 1 and 10?!  Then guess away:\n")
counter = 0
##^this counter = 0 line was in the while loop, making counter always 0 + 1.  Ouside of the loop, it doesn't overwrite counter every single time.
odd_run = True #before the while loop runs, the first_run is True
even_run = True
while True:
    counter = counter + 1
    user_guess = int(input(f"Guess a number:\n\n"))
    print(f"Your guess is {user_guess}.\n")
    if user_guess == comp_num:
        print(f"Congratulations, you indeed have the gift!  YOU could guess the number {comp_num} with your mind.\n\nAnd it only took you {counter} tries!\n\nThanks for playing!")
        break
    elif user_guess > comp_num:
        print(f"I'm sorry.  Your guess is too high!  Try a lower number.\n")
    elif user_guess < comp_num:
        print(f"I'm sorry.  Your guess is too low!  Try a higher number.\n")
    if odd_run == True and even_run == True:  ##These warmer/colder lines for Advanced 4 aren't quite right##
        close_odd = abs(comp_num - user_guess)
        odd_run = False
    elif even_run == True and odd_run == False:
        close_even = close_odd
        close_even = abs(comp_num - user_guess)
        if close_odd < close_even:
            print("And you're getting colder...\n\n")
        if close_odd > close_even:
            print("But you're getting warmer...\n\n")
        odd_run = True
        even_run = False
    else:        ##I commented out all these lines because it just doesn't work right
        close_odd = close_even
        close_even = abs(comp_num - user_guess)
        if close_odd < close_even:
            print("And you're getting colder...\n\n")
        if close_odd > close_even:
            print("But you're getting warmer...\n\n")  ##They work sometimes and I kinda get what the problem is but not how to fix it##
        even_run = True
        odd_run = False
    if counter == 10: #I had this line as an else and and elif.  Neither worked.  You can start a new if whenever!
        print("I'm sorry, you've tried 10 times and couldn't get it...  I don't think you have the gift.\n\n")
        break
    # else:  ##These 2 lines didn't work out with the advanced version so I commented out
    #     print("I am so sorry...  You don't have the gift at all.\n\nTry your luck again!\n\n")

##Adv Ver 1: Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.

##Adv Ver 2:  Keep track of how many guesses the user has made, and tell them at the end.

##Adv Ver 3: Using a while loop, allow the user to guess 10 times.  If they fail to guewss the number after 10 tries, the user is told they've lost.

##Adv Ver 4: Tell the user whether their current guess is closer than their last.
