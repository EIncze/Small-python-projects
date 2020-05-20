#! python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 21:53:29 2020

@author: Eddie
"""
import random, sys, nltk
from nltk.corpus import gutenberg#, words
from nltk.probability import FreqDist

stopwords = nltk.corpus.stopwords.words('english')
allWordExceptStopDist = FreqDist(w.lower() for w in gutenberg.words() if (w not in stopwords) and (len(w) > 4))

print('\n\nH A N G M A N')
print('Type "exit" at any time to quit:')
print('The difficulty can be set by typing a number x, enabling the x*1000 most common words for the program to choose from.')
worddifficulty = 1000* int(input('Select difficulty level: '))
if worddifficulty == 'exit':
        sys.exit()
        
mostCommon= allWordExceptStopDist.most_common(worddifficulty)
correctword = mostCommon[random.randint(0,(len(mostCommon)))][0]
correctlist = list(correctword)
guesses = set()
lives = 10
        
print('\n'+'-'*(len(correctword)))

while lives > 0:
    guess = input('Input a letter: ').lower()
    if guess == 'exit':
        sys.exit()
    if guess == correctword:
        print('Congratulations, you guessed it!')
        break
    if len(guess) != 1:
        print('You should print a single letter')    
    elif (not guess.islower()):
        print('It is not an ASCII lowercase letter')
    elif guess in guesses:
        print('You already typed this letter') 
    elif guess not in correctlist:
        lives -= 1
        print(f'No such letter in the word. You have {lives} lives left.')
    guesses.add(guess)  
    hint = ''.join([letter if letter in guesses else '-' for letter in correctlist])
    if hint == correctword:
        print(f"You guessed the word {correctword}!\nYou survived!")
        break 
    elif lives == 0:
        print(f'The word was: {correctword}\n You are hanged')
        break

    print('\n',hint)