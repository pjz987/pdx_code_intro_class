'''
filename: madlibs.py (Lab 2)
concepts:
    - print()
    -Datatype: strings
    -input()
'''
#user greeting
print("Welcome to Mad Libs! \n")


# Input
animal = input("Name an animal: ")
part_of_house = input("Name a part of a house: ")
bad_weather = input("Name a type of bad weather: ")
good_weather = input("Name a type of good weather: ")

print() # prints empty line
print("Here is your MadLib \n")
# Output
print(f"The itsy bitsy {animal} went up the water {part_of_house}.  Down came the {bad_weather} and washed the {animal} out.  Out came the {good_weather} and dried up all the {bad_weather} and the itsy bitsy {animal} climbed up the {part_of_house} again.")
