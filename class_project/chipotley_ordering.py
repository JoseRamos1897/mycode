#!/usr/bin/env python3

import datetime


def chipotley_ordering_system():
   
    ######## GREETING/OPTIONS/PRICES ########
    
    print('Welcome to chipotley!\n')
    entrees = {'burrito': 10.00, 'taco': 5.00, 'bowl': 9.00}
    toppings = {'fresh salsa': .50, 'GUAC': 3.50, 'cheese': 1.15, 'corn': 1.00, 'lettuce': .50}
    proteins = {'chicken': 3.00, 'steak': 4.50, 'vegan': 4.75}

    ######## CHOOSING ENTREE ########

    print('These are our entree options:\n')
    for entree in entrees:
        print(entree)
    entree_pick = input('\nWhat entree would you like? \n').lower()
    print(f'The {entree_pick} is my favorite! great choice!\n')
   
    ####### CHOOSING PROTEIN ########
   
    print('These are your choices for protein.\n')
    for protein in proteins:
        print(protein)
    protein_pick = input('\nWhat protein would you like? ')
    if protein_pick == 'vegan':
            print(f'\nEWWWW!! {protein_pick} is disgusting.. but okay.')
    elif protein_pick == 'chicken' or 'steak':
            print(f'\nI love {protein_pick}! We have so much in common..')

    ####### CHOOSING SINGLE TOPPING #######
    
    print('\nNow it is time to pick your topping. You can only choose one.. so choose wisely.\n')
    for topping in toppings:
        print(topping)
    toppings_pick = input('\nWhich topping would you like? \n').upper()
    print(f'Our {toppings_pick} is the best in town!\n')
    if toppings_pick == 'GUAC':
        baller = input('It\'s pretty pricey though. You sure you want some? ')
        if baller == 'yes':
            print(f'\nOkay big baller. You got it!')
        elif baller == 'no':
            print(f'\nGet your money up chump')
    
    ####### ORDER REVIEW AND TOTAL #######
    
    total = entrees[entree_pick] + proteins[protein_pick] + toppings[toppings_pick]
    print(f'\nPlease review your order:\n\n{entree_pick} with {protein_pick} protein and {toppings_pick} topping.')
    order_review = input(f'\nDoes this look right? ')
    if order_review == 'yes':
        print(f'\nSounds great, your total is ${total}')
    else:
        print(f'\nToo bad.. we are not starting over, your total is ${total}')

    ####### WRITE SALES STATS TO FILE #######

    with open('chipotley_stats.txt', 'a') as stats:
        print(entree_pick , protein_pick , toppings_pick, datetime.date.today(), file = stats)
    
chipotley_ordering_system()
