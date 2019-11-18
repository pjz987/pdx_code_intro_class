'''
filename: enough_sleep.py

'''
user_sleep = input("How much did you sleep? ")
user_sleep = int(user_sleep)
if user_sleep < 4:
    print("Go back to sleep!")
if user_sleep > 12:
    print("Are you dead?")
if user_sleep >= 4 and user_sleep <= 12:
    print("Great job!")

 ### You need '' around integers
 ### Or put int() around the variable
