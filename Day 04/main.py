import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

winning_conditions = {
    (0, 2): True, # rock beats scissors
    (1, 0): True, # paper beats rock
    (2, 1): True  # scissors beats paper
}

# Determine the winner
if player_choice == computer_choice:
    result = "It's a draw!"
elif (player_choice, computer_choice) in winning_conditions:
    result = "You win!"
else:
    result = "You lose!"

print(f"You chose:\n{[rock, paper, scissors][player_choice]}")
print(f"The computer chose:\n{[rock, paper, scissors][computer_choice]}")
print(result)