#! python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:36:40 2020

@author: Eddie
"""
import sys


class CoffeeMachine:
    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.supply = [water, milk, beans, cups, money]

    def take_request(self, request):
        if request == 'buy':
            self.buying()
        elif request == 'fill':
            self.filling()
        elif request == 'take':
            self.taking()
        elif request == 'remaining':
            self.remaining()
        elif request == 'exit':
            sys.exit()

    
    def buying(self):
        choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if choice == 'back':
            self.take_request(input('Write action (buy, fill, take, remaining, exit):\n'))
            return None
        choice = int(choice)
        canserve = True
        for i in range(0,4):        
            if self.supply[i] < coffeesupplies[choice-1][i]:
                print(f'Sorry, not enough {supplies[i]}!')
                canserve = False
                break
        if canserve:
            print('I have enough resources, making you a coffee!')
            self.supply[0:4] = [x-y for x,y in zip(self.supply, coffeesupplies[choice-1])]
            self.supply[4] += price[choice-1]
                
    def filling(self):
        self.supply[0] += int(input('Write how many ml of water do you want to add:\n'))
        self.supply[1] += int(input('Write how many ml of milk do you want to add:\n'))
        self.supply[2] += int(input('Write how many grams of coffee beans do you want to add:\n'))
        self.supply[3] += int(input('Write how many disposable cups of coffee do you want to add:\n')) 

    def taking(self):
        print(f'I gave you ${self.supply[4]}')
        self.supply[4] = 0

    def remaining(self):
        print(f'''\nThe coffee machine has:
                \n{self.supply[0]} of water
                \n{self.supply[1]} of milk
                \n{self.supply[2]} of coffee beans
                \n{self.supply[3]} of disposable cups
                \n${self.supply[4]} of money''')


coffees = {1 : 'espresso', 2 : 'latte', 3 : 'cappuccino' }
supplies = {0 : 'water', 1 : 'milk', 2 : 'beans', 3 : 'cups'}
espresso = (250,0,16,1)
latte = (350,75,20,1)
cappuccino = (200,100,12,1)
coffeesupplies = (espresso, latte, cappuccino)
price = [4,7,6]


cm = CoffeeMachine()
while True:
    cm.take_request(input('Write action (buy, fill, take, remaining, exit):\n'))