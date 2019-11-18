'''
filename: lab05_emoticon.py
Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth.
'''

# 1. Define a list of eyes
eyes = [':', ';']

# 2. Define a list of noses
noses = ['<', '>', '^']

# 3. Define a list of mouths
mouths = ['(', ')', '/', '|', '#']

# 4. Randomly pick a set of eyes
import random
eye = random.choice(eyes)

# 5. Randomly pick a nose
nose = random.choice(noses)

# 6. Randomly pick a mouth
mouth = random.choice(mouths)

# 7. Assemble and display the emoticons

print(eye+nose+mouth)


'''
Advanced Version 1
Use a for loop to generate 5 emoticons
'''

emotes_5 = ''
for num in range(5):
    emotes_5 = emotes_5 + random.choice(eyes) + random.choice(noses) + random.choice(mouths) + ' '
print (emotes_5)
