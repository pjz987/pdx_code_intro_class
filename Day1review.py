'''
Day 02: Review of Day 01

- comments
  - single
  - multi-line
- print
  -concatenating
  -fstrings
-variables
-input()
'''

### Comments ###
# This is a comment
# You create a comment with a "#" sign at the beginning of a line
# great for notes

### Multi Line Comment ###
'''
Triple apostrophes will allow you
to write multi line quotes
great for sharing a ton of info with your team
make sure you start and end with THREE quotes
'''

print("Hello!")

### Variables ###
# variables hold data

# fav_color is the variable name
# "=" is an assignment operator
# "red" is the data and the datatype is String
fav_color = "red"

'''
helpful hints for naming Variables
- lowercase
- use underscores instead of dashes
  - fav_color vs fav-color
- and definitely no spaces
'''

### print() ###
'''
- print() is a function that renders data to the console (user)
'''

# printing string directly in print() statement. ex:
print("Hello World!")

# print variables in print statement
# if just the variable, no fstring
print(fav_color)

# if variable + Stringprint("My favorite color is " + fav_color)

# or use fstring

print(f"Myfavorite color is {fav_color} because of Winnie the Pooh's shirt.")

### input ###
# input() prompt to input data
# won't move on until user hits enter on keyboard
fav_color2 = input("What is your second favorite color? ")

print(f"Cool!  Your second favorite color is: {fav_color2}")
