# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 22:43:38 2022

@author: 20CE013
"""

t = int(input()) # User Input: No. of Test Cases

li = [] # Empty List

for i in range(4): # Taking Strings from User
    li.append(input())

li_dict = list(dict.fromkeys(li)) # Removing Repeating Elements

print(len(li_dict)) # Printing Number of Non Repeating Elements

for i in li_dict: # Printing Counts of every element Repeated in List
    print(li.count(i), end = " ")

print() # New Line

# Student ID: 20CE13
# Student Name: Chovatiya Mayank
# Aim: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output 
#     order should correspond with the input order of appearance of the word. See the sample input/output for 
#     clarification. 