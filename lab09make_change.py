'''
filename : lab09make_change.py
Lab 09: Make Change
Let the user enter how many pennies they have, and convert their pennies into larger coins and leftover pennies.
##Advanced Versions 1 & 2##
'''
import random #always do this first when you need it
# pennies = int(input("Welcome to the bank where we convert your pennies into larger coins. How many pennies do you have? "))
# dollars = pennies // 100 #I did dollars too for fun
# pennies = pennies % 100
dollar_amount = float(input("Welcome to the bank where we convert your cash into coins so you have heavy coins in your pockets.\nWhat is the dollar amount you'd like converted? $"))
first_run = True
while True:
    pennies = dollar_amount * 100
    print(f"\nWow, that's {int(pennies)} pennies... so...")
    # print(dollar_amount)            ## These were from learning float()
    # print(round(dollar_amount, 2))  ## and (round)
    ##quarters V1 Convert the user's pennies into the maximum number of quarters
    quarters = pennies // 25
    pennies = pennies % 25
    ##dimes nickels V2 Also convert to dimes and nickels
    dimes = pennies // 10
    pennies = pennies % 10
    nickels = pennies // 5
    pennies = pennies % 5
    print(f"You now have {int(quarters)} quarters, {int(dimes)} dimes, {int(nickels)} nickels, and {int(pennies)} pennies in your pockets.\nThanks for coming to the bank where we convert your cash into coins so you have heavy coins in your pockets.")
    add_sub = input("Would you like to (add) or (subtract) a dollar amount to the heavy coins in your pockets? ").lower()
    if add_sub == 'add':
        add = float(input("How much would you like to add? $"))
        dollar_amount = dollar_amount + add
        print(f"Okay, your dollar amount is now ${round(dollar_amount, 3)}...")##confused how to make those zeros show up i.e. ($6.90 instead of just $6.9)
        continue
    if add_sub == 'subtract':
        sub = float(input("How much would you like to subtract? $"))
        dollar_amount = dollar_amount - sub
        print(f"Okay, your dollar amount is now ${round(dollar_amount, 3)}...")##confused how to make those zeros show up i.e. ($6.90 instead of just $6.9)
        continue
    else:
        break
