'''
filename : pie.py
#if #
'''
import random

#through import in at the top if you need it

pie_list = ['pumpkin', 'keylime']
ingredient_list = ['pumpkins', 'keylimes']
while True:
    user_pie = input("What pie would you like to make? ").lower()
    if user_pie in ['pumpkin', 'keylime']:
        break
#.lower() makes the user input lowercase
in_season = random.choice(ingredient_list)
print(f"{in_season} are in season")
if user_pie == 'pumpkin':
    if in_season == 'pumpkins':
        print("Yum! Thanksgiving pie!")
    if in_season == 'keylimes':
        print("Bad time for pumpkin pie.")
if user_pie == 'keylime':
    if in_season == 'keylimes':
        print("Great time for lime!")
    if in_season == 'pumpkins':
        print("Wouldn't you prefer pumpkin?")
