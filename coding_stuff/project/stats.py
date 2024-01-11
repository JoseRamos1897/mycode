#!/usr/bin/env python3

def check_stats():
    print('Hello! This tool can help you determine how many times a specific item was ordered in a given month.')
    month = input('Choose enter the two digit month: ')
    item = input('Choose an item: ')
    counter = 0


    with open('chipotley_stats.txt', 'r') as file:
        for line in file:
            if month and item in line:
                counter += 1
    
    print(f'{item} was order {counter} times in the month of {month}')

check_stats()

