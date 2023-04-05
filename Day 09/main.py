import os
from subprocess import call
from art import *

def clear():
    _ = call('clear' if os.name =='posix' else 'cls')
    
def get_winner(bidders):
    winner = max(bidders, key=bidders.get)
    print(f'The winner is {winner} with a bid of ${bidders[winner]}')

print(logo)
print('Welcome to the silent auction!')

bids = {}

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if answer == 'no':
        break
    clear()

get_winner(bids)
