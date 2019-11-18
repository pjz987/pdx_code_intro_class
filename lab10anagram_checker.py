'''
filename : lab10anagram_checker.py
Lab 10: Anagram Checker
Let's write an anagram checker.
'''

'''
Anagram
Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. dormitory and dirty room.

Write a program that lets the user enter two strings, and tells them if they are anagrams of each other.
'''
import string
word1 = list(input("Welcome to the Anagram Checker.  We're going to check if two different words are anagrams to each other.\n\nEnter the first word: ").lower().replace(' ', ''))##Adv Ver 1 lower() and replace()--(to remove spaces)
word2 = list(input("Enter the second word: ").lower().replace(' ', ''))##Adv Ver 1 lower() and replace()--(to remove spaces)
print()
# for string.punctuation in word1: ##ATTEMPT at AdVer2
#     word1 = word1.replace(string.punctuation, '')
#     #word2.replace(punct, '')
# print(word1)
word1.sort()
word2.sort()
if word1 == word2:
    print("They're anagrams.")
else:
    print("They're not anagrams.")

'''
Advanced Version 2 ###### Could not figure this one out
Make your program ignore punctuation when checking anagrams...
'''
