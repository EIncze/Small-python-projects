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
        if key.title() in data.keys():
            return data[key.title()]
        elif key.upper() in data.keys():
            return data[key.upper()]
        else:
            try:
                a, b, c = get_close_matches(key.lower(), data.keys(), n=3, cutoff=0.6)
                choice =  input(f'Did you mean {a.lower()}? (Press Y for "Yes" or N for "No") ')
                if choice.lower() == 'y':
                    return data[a]
                elif input(f'Did you mean {b}? (Press Y for "Yes" or N for "No") ').lower() == 'y':
                    return data[b]
                elif input(f'Did you mean {c}? (Press Y for "Yes" or N for "No") ').lower() == 'y':
                    return data[c]
                else:
                    return 'Please check your spelling and try again'
            except ValueError:
                return grabber(input('Please enter a valid word: '))



while True:
    out = grabber(input("Please enter word: "))
    if type(out) == list:
        for item in out:
            print(item)
    decide = input('Would you like to try another? Press Y for "Yes", or any other key to exit ').lower()
    if decide != 'y':
        break
