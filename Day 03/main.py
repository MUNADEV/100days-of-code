print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Adventure.\n")
print("Your mission is to find the treasure.\n") 
print("You find an old map that leads to a hidden treasure deep in the jungle.")
print("After a long and perilous journey, you arrive at a clearing.\n")

direction = input('You see a small stream to your left and a narrow path leading to the right. Which way do you choose? Type "left" or "right": \n').lower()
if direction == "left":
    action = input("You choose to go left and follow the stream. After a while, you come across a fallen tree that blocks the path. You can try to climb over it or find a way around. Type 'climb' or 'around': \n").lower()
    if action == "climb":
        print("As you reach the top, you slip and fall down, twisting your ankle.")
        action = input("You can continue on or turn back. Type 'continue' or 'turn back': \n").lower()
        if action == "continue":
            print("Soon, you see the entrance to a cave.")
            action = input("You can either explore the cave or rest and tend to your injury. Type 'explore' or 'rest': \n").lower()
            if action == "explore":
                print("Inside, you see three tunnels.")
                direction = input("One to the left, one to the right, and one straight ahead. Which way do you choose? Type 'left', 'right', or 'straight': \n").lower()
                if direction == "straight":
                    print("After a while, you see a glimmer of light up ahead. You run towards it and find the treasure! You Win!")
                else:
                    print("You entered a tunnel that leads to a dead end. Game Over.")
            else:
                print("You decided to rest and tend to your injury. While resting, a pack of wild animals attacked you. Game Over.")
        else:
            print("You turned back and got lost in the jungle. Game Over.")
    else:
        print("You found a way around the fallen tree.")
else:
    print("The narrow path is a trap and you are caught by cannibals to eat you. Game Over")

           
