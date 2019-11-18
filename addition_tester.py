'''
filename : addition_tester.py
'''

import random
num1 = random.randint(1,5)
num2 = random.randint(1,5)
while True:
    user_guess = int(input(f"What is {num1} + {num2}? "))
    if num1 + num2 == user_guess:
        print('correct')
        break
    else:
        print('try again')
    num1 = random.randint(1,5)
    num2 = random.randint(1,5)
