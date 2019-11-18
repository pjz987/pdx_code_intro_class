'''
filename: song_gen.py
'''

# Version 1
import random
notes = ['da', 'do', 'de']
print (random.choice(notes) + random.choice(notes) + random.choice(notes))

# Version 2
out_string = ''
for num in range(10):
    out_string = out_string + random.choice(notes)
print(out_string)
