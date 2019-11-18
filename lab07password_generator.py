'''
filename : lab07password_generator.py

Lab 7: Password Generator

Let's generate a password ten characters long using a loop (while loop or for loop) and random.choice, this will be a string of random characters.
'''

#always import random first if needed
import random
#using import string to quickly call up alphabet/numbers
import string

pass_length = input("How many characters do you want in your password?\n")

pass_length_int = int(pass_length)
#^I needed int() to turn the string pass_length into the integer pass_length_int
password = ''
for characters in range(pass_length_int):
    characters = string.ascii_lowercase + string.digits + string.punctuation + string. ascii_uppercase
    #^ was characters = [string.ascii_lowercase + string.digits] the brackets made it not work right
    password = password + random.choice(characters)
print(password)

'''
Advanced Version 1
Allow the user to choose how many characters the password will be.
##I went back and added this code starting on line 14.##
'''

'''
Advanced Version 2
Allow the user to choose how many letters, numbers, and punctuation characters they want in their password.  Mix everything up using list(), random.shuffle(), and ''.join().
##^figure out what this is about some other day^##
'''
