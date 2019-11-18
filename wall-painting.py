'''
filename: wall-painting.py

Lab 11: Wall Painting

Create a new file wall-painting.py

All our friends are re-painting one wall of their rooms.  They want us to figure out how much it's going to cost.  Assume one gallon of paint covers 400 square feet.

Ask the user for:

    1. width of the wall
    2. height of the wall
    3. how much a gallon of paint costs

Figure out then print how much it will cost to paint the wall with one coat.
'''
import math

walls = int(input("\nHow many walls are you painting? "))
count = 1

width = int(input(f"\nWhat is the width (ft) of wall {count}? "))
height = int(input(f"\nWhat is the height (ft) of wall {count}? "))

#Advanced3 Allow the user o enter multiple wall dimensions and it adds the total areas together before calculating the cost.
while walls > count:
    count = count + 1
    width = width + int(input(f"\nWhat is the width (ft) of wall {count}? "))
    height = height + int(input(f"\nWhat is the height (ft) of wall {count}? "))

#Advanced1 Also ask the user for how many coats they're going to put on, and calculate that cost.
coats = int(input("\nHow many coats? "))
gallon_cost = int(input("\nAnd how much does a gallon of paint cost? $"))

#Advanced2 You can only buy whole gallons of paint. Figure out away to round up so that you know how many whole gallons to buy.
gallons = math.ceil((width * height * coats) / 400)

cost = gallons * gallon_cost

print(f"\nIt will cost ${cost} to buy {gallons} gallon(s) to paint the wall with {coats} coat(s).")
