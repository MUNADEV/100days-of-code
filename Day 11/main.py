from operator import truediv
from random import choice
from subprocess import call
from art import *
from os import system, name
import random
 # import sleep to show output for some time period
from time import sleep
 
# define our clear function
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def deal_cards(num_of_cards):
  """Returns a list of random cards from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.sample(cards, num_of_cards)

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  score = sum(cards)
  if score > 21 and 11 in cards:
    score -= 10
  return score

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 21:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 21:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  print(logo)
  user_cards = deal_cards(2)
  computer_cards = deal_cards(2)
  is_game_over = False

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 21 or computer_score == 21 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards += deal_cards(1)
      else:
        is_game_over = True

  while computer_score < 17 and not is_game_over:
    computer_cards += deal_cards(1)
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
