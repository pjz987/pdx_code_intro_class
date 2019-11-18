'''
filename : candy_betting.py
'''
import random
candy = 0
pennies = random.randint(200,300)
while True:
    choice = input("Type (bet) or (cash out): ").lower()
    if choice != 'bet':
        break
    bet_amount = int(input("Bet how many quarters?: "))
    if bet_amount * 24 > pennies:
        continue
    if random.choice(['heads', 'tails']) == 'heads':
        print("You win")
        candy = candy + bet_amount
    else:
        print("You lose")
        pennies = pennies - (bet_amount * 25)
candy = candy + (pennies // 25) ##division #just one / is division w/o separating the remainder
pennies = pennies % 25 ##remainder
print(f"You finished with {candy} candy and {pennies} pennies.")
