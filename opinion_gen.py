'''
filename: opinion_gen.py
    -learning objective: import - connects to a module
    -a module is a library or collection of functions
'''
# import connects to the random module
import random

# fav_movie is a variable where we saved input from the user after asking them a question

fav_movie = input("What is your favorite movie?...")

# list variable
# variable_name = []
# literally a list of items: grocery list, opinions, states, etc.
# opinion_list = ["ok", "great", "why would you watch that?", "fantastic", "amazing", "straight trash"]

### sample lists for testing ###
fav_colors = ["red", "black", "orange"]

groceries = ["Bloody Mary mix", "navel oranges", "limes", "lemons", "ginger beer"]

selection = random.choice(groceries)

print(selection)
