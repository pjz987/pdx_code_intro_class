'''
filename : favorite_colors.py
'''

favorite_colors = ['green', 'yellow', 'blue']

color_guesses = []
while len(color_guesses) < len(favorite_colors):
    one_guess = input('Guess one of my favorite colors: ').lower()
    color_guesses.append(one_guess)
favorite_colors.sort()
color_guesses.sort()
if favorite_colors == color_guesses:
    print("Correct!")
