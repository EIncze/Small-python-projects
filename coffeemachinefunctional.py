#! python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:36:40 2020

@author: Eddie
"""
import sys

supply = [400,540,120,9,550]
#water, milk, beans, cups, money
coffees = {1 : 'espresso', 2 : 'latte', 3 : 'cappuccino' }
supplies = {0 : 'water', 1 : 'milk', 2 : 'beans', 3 : 'cups'}
espresso = (250,0,16,1)
latte = (350,75,20,1)
cappuccino = (200,100,12,1)
coffeesupplies = [[250,0,16,1],[350,75,20,1],[200,100,12,1]]
price = [4,7,6]

while True:
    canserve = True
    action = input('Write action (buy, fill, take, remaining, exit):\n')
    if action == 'buy':
        choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if choice == 'back':
            continue
        else:
            choice = int(choice)
        for i in range(0,4):        
            if supply[i] < coffeesupplies[choice-1][i]:
                print(f'Sorry, not enough {supplies[i]}!')
                canserve = False
                break
        if canserve:
            print('I have enough resources, making you a coffee!')
            supply[0:4] = [x-y for x,y in zip(supply, coffeesupplies[choice-1])]
            supply[4] += price[choice-1]
            
    elif action == 'fill':
        supply[0] += int(input('Write how many ml of water do you want to add:\n'))
        supply[1] += int(input('Write how many ml of milk do you want to add:\n'))
        supply[2] += int(input('Write how many grams of coffee beans do you want to add:\n'))
        supply[3] += int(input('Write how many disposable cups of coffee do you want to add:\n'))    
    elif action == 'take':
        print(f'I gave you ${supply[4]}')
        supply[4] = 0
    elif action == 'remaining':
        print(f'''\nThe coffee machine has:
            \n{supply[0]} of water
            \n{supply[1]} of milk
            \n{supply[2]} of coffee beans
            \n{supply[3]} of disposable cups
            \n${supply[4]} of money''')
    elif action == 'exit':
        sys.exit()
    