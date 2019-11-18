'''
filename: pattern_gen.py
'''

import random
pattern_list = ['##', '%%', '$$', '//', '\\\\']
out_string = ''
for item in range(10):
    out_string = out_string + random.choice(pattern_list) * 5
    out_string = out_string + '\n'
print(out_string)
