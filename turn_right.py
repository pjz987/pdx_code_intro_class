# turn_right.py
import random
direction_list = ['North', 'East', 'South', 'West']
start = random.randrange(len(direction_list))
print(f"You are facing {direction_list[start]}")
turns = int(input("Turn right how many times? "))
end = start + turns
print(f"You are facing {direction_list[end % len(direction_list)]}")
