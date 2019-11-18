'''
filename : unit_converter.py

Lab 12: Unit Converter
This lab will involve writing a program that allows the user to convert a number between units.
'''

'''
Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by *multiplying the input distance by 0.3048*. Below is some sample input/output.
    > what is the distance in feet? 12
    > 12 ft is 3.6576 m
'''

'''
Version 2
Allow the user to also enter the units. Then dependgin on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
    1 ft is 0.3058 m
    1 mi is 1609.34 m
    1m is 1m
    1 km is 1000 m
Below is some sample input/output:
    > what is the distance? 100
    > what are the units? mi
    >100 mi is 160934 m
'''

'''
Version 3
Add support for yards and inches.
    1 yard is 0.9144 m
    1 inch is 0.0254
'''

'''
Version 4
Allow the user to choose the unit to convert to.
'''

unit1 = input("\nWelcome to the Unit Converter.  What unit would you like to convert from? Please enter in, ft, yd, mi, m, or km: ")
if unit1 == 'in':
    conv1 = .0254
if unit1 == 'ft':
    conv1 = .3048
if unit1 == 'yd':
    conv1 = .9144
if unit1 == 'mi':
    conv1 = 1609.34
if unit1 == 'm':
    conv1 = 1
if unit1 == 'km':
    conv1 = 1000
unit2 = input("\nWhat unit would you like to convert to? Please enter in, ft, yd, mi, m, or km: ")
dist1 = int(input(f"\nHow many {unit1} would you like to convert to {unit2}? "))
if unit2 == 'in':
    conv2 = 39.37
if unit2 == 'ft':
    conv2 = 3.2808
if unit2 == 'yd':
    conv2 = 1.0936
if unit2 == 'mi':
    conv2 = .0006
if unit2 == 'm':
    conv2 = 1
if unit2 == 'km':
    conv2 = .001
dist2 = round((dist1 * conv1 * conv2), 4)
print(f"\n{dist1} {unit1} is {dist2} {unit2}. Thanks.")
