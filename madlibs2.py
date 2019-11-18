### My fairytale MadLibs ###
'''
file name madlibs2.py three little pigs
'''
#user greeting
print("Welcome to Three Little Pigs Mad Libs! \n")

# Input
# name
your_name = input("What's your name? ")

print()

# 5 nouns
noun_1 = input("Noun, please! ")
noun_2 = input("Another noun, yo! ")
noun_3 = input("Keep the nouns comin'! ")
noun_4 = input("Another one, you know the drill! ")
noun_5 = input("Last one please! ")

print()

# 3 adjectives
adjective_1 = input("Okay, smart fellow, now give me an adjective! ")
adjective_2 = input("Another! ")
adjective_3 = input("One last adjective! ")

print()

# 7 verbs
verb_1 = input("Okay let's hear your verbs ")
verb_2 = input("You gotta name 7 altogether ")
verb_3 = input("Keep the verbs comin' ")
verb_4 = input("Verb! ")
verb_5 = input("Again! ")
verb_6 = input("Again! ")
verb_7 = input("One more! ")

print()

# 3 plural nouns
plural_noun_1 = input("Okay now some plural nouns ")
plural_noun_2 = input("Keep them coming, 2 more ")
plural_noun_3 = input("One more plural noun, please ")

print()

# 6 past tense verbs
past_tense_verb_1 = input("Okay, genious, now your best past tense verbs! ")
past_tense_verb_2 = input("Keep them coming! ")
past_tense_verb_3 = input("Again! ")
past_tense_verb_4 = input("Again! ")
past_tense_verb_5 = input("Again! ")
past_tense_verb_6 = input("Last One! ")

print()

print("Thanks for providing 21(!) different words.  Here is your Mad Lib \n")
# Output
# Title
print("Three Little Pigs\n")
# Byline
print(f"by: {your_name}\n")
# Story
print(f"Once upon a time, there were three {adjective_1} pigs.  One day, their mother said, You are all grown up and must {verb_1} on your own.  So they left to {verb_2} their houses.  The first little pig wanted only to {verb_3} all day and built his house out of {plural_noun_1}.  The second little pig wanted to {verb_4} and {verb_5} all day so he {past_tense_verb_1} his house with {plural_noun_2}.  The third {adjective_2} pig knew the wolf lived nearby and worked hard to {verb_6} his house out of {plural_noun_3}.  One day, the wolf knocked on the first pig's {noun_1}.  Let me in or I'll {verb_7} your house down!  The pig didn't, so the wolf {past_tense_verb_2} down the {noun_2}.  The wolf knocked on the second pig's {noun_3}.  Let me in or I'll blow your {noun_4} down!  The pig didn't, so the wolf {past_tense_verb_3} down the house.  Then the wolf knocked on the third {adjective_3} pig's door.  Let me in or I'll blow your house down!  The little pig didn't so the wolf {past_tense_verb_4} and {past_tense_verb_5}.  He could not blow the house down.  All the pigs went to live in the {noun_5} house and they all {past_tense_verb_6} happily ever after.\n")
print("The End")
