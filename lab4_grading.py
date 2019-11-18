'''
filename: lab4_grading.py
Convert a nubmer grade to a letter grade, using if and elif statements and comparisons.
'''

#1. Have the user enter a number representing a grade (0-100)
ug_num = input("\nEnter your grade percentage number: ")

ug_num = int(ug_num)

print(f"\nYour Number Grade is {ug_num}% so your Letter Grade is...\n")

#2. Convert the number grade to a letter grade.

if ug_num >= 90 and ug_num <= 100:
    ug_lett = 'A'
if ug_num >= 80 and ug_num <= 89:
    ug_lett = 'B'
if ug_num >= 70 and ug_num <= 79:
    ug_lett = 'C'
if ug_num >= 60 and ug_num <= 69:
    ug_lett = 'D'
if ug_num >= 0 and ug_num <= 59:
    ug_lett = 'F'

#Advanced 2 this line to...#
ug_rem = ug_num % 10
if ug_rem in range(0, 3):
    ug_plus_min = '-'
if ug_rem in range(3, 7):
    ug_plus_min = ''
if ug_rem in range(7, 10):
    ug_plus_min = '+'
if ug_lett == 'F':
    ug_plus_min = ''
if ug_lett == 'A':
    if ug_rem in range(3,10):
        ug_plus_min = ''
if ug_num == 100:
    ug_plus_min = ''
#...this line Advanced 2#
print(f"{ug_lett}{ug_plus_min}")

'''
Advanced Version 1
Use randint() from the random module to determine the user's rival's score. Let the user know if they did better than their rival.
'''

import random
rg_num = random.randint(0,100)

print(f"\nYour rival's Number Grade is {rg_num}% so your rival's Letter Grade is...\n")

if rg_num >= 90 and rg_num <= 100:
    rg_lett = 'A'
if rg_num >= 80 and rg_num <= 89:
    rg_lett = 'B'
if rg_num >= 70 and rg_num <= 79:
    rg_lett = 'C'
if rg_num >= 60 and rg_num <= 69:
    rg_lett = 'D'
if rg_num >= 0 and rg_num <= 59:
    rg_lett = 'F'

#Advanced 2 This line to...##
rg_rem = rg_num % 10
if rg_rem in range(0, 3):
    rg_plus_min = '-'
if rg_rem in range(3, 7):
    rg_plus_min = ''
if rg_rem in range(7, 10):
    rg_plus_min = '+'
if rg_lett == 'F':
    rg_plus_min = ''
if rg_lett == 'A':
    if rg_rem in range(3,10):
        rg_plus_min = ''
if rg_num == 100:
    rg_plus_min = ''

print(f"{rg_lett}{rg_plus_min}")
##... this line Advanced 2##
print()
if ug_num >= rg_num:
    print("Congratulations.  You did better than your rival!\n")
if ug_num <= rg_num:
    print("Sorry.  Your rival did better than you...\n")
if ug_num == rg_num:
    print("You and your rival did equally well.\n")
