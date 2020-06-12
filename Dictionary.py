# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:38:54 2018
@author: Eddie
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))


def grabber(key):
    try:
        return data[key.lower()]
    except KeyError:
        try:
            a, b, c = get_close_matches(key.lower(), data.keys(), n=3, cutoff=0.6)
            if a == key.title():
                return data[key.title()]
            elif key.upper() in data: 
                return data[key.upper()]
            choice =  input('Did you mean %s? (Press Y for \'Yes\' or N for \'No\') ' %a).lower()
            if choice == 'y':
                return data[a]
            elif input('Did you mean %s? (Press Y for \'Yes\' or N for \'No\') ' %b).lower() == 'y':
                return data[b]
            elif input('Did you mean %s? (Press Y for \'Yes\' or N for \'No\') ' %c).lower() == 'y':
                return data[c]
            else:
                return 'Please check your spelling and try again'
        except ValueError:
            return grabber(input('Please enter a valid word: '))


word = input("Please enter word: ")
out = grabber(word)
if type(out) == list:
    for item in out:
        print(item)
decide = 'y'
while decide == 'y':
    decide = input('Would you like to try another? Press Y for \'Yes\', or any other key to exit ').lower()
    if decide != 'y':
        break
    out = grabber(input("Please enter word: "))
    if type(out) == list:
        for item in out:
            print(item)
