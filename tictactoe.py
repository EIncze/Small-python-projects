#! python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:25:50 2020

@author: Eddie
"""
import sys

cells = ','.join(' '*9).split(',')
cellsarray = [cells[i:i+3] for i in range(0,len(cells),3)]

turn=1

def print_state(cells):
    print(f'''
{'-'*9}
| {' '.join(cells[:3])} |
| {' '.join(cells[3:6])} |
| {' '.join(cells[6:])} |
{'-'*9}
''')

print_state(cells)


def check_state():
    if 'XXX' in state:
        print('X wins')
        sys.exit()
    elif 'OOO' in state:
        print('O wins')
        sys.exit()
    elif turn == 10:
        print('Draw')
        sys.exit()
        
while True:
    usercoords = input('Enter the coordinates: ').split(' ')
    
    try:
        usercoords[0] = int(usercoords[0])
        usercoords[1] = int(usercoords[1])
    except:
        print('You should enter numbers!')
        continue
    
    if (usercoords[0] not in range(4)) or (usercoords[1] not in range(4)):
        print('Coordinates should be from 1 to 3!')
        continue
    
    row = 3 - usercoords[1]
    column = usercoords[0] - 1

    if cellsarray[row][column] in ['X', 'O']:
        print('This cell is occupied! Choose another one!')
        continue
    
    if turn % 2:
        cellsarray[row][column] = 'X'
    else:
        cellsarray[row][column] = 'O'
        
    turn +=1
    cells = ''.join([elem for inner in cellsarray for elem in inner])
    state = [cells[:3], cells[3:6], cells[6:], cells[:7:3], cells[1:8:3], cells[2::3], cells[::4], cells[2:8:2]]
    print_state(cells)
    check_state()
    




