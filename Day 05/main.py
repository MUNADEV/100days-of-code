#Password Generator Project

#import random
#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random
import string

# define the characters, best way
letters = string.ascii_letters
symbols = string.punctuation
numbers = string.digits

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

# instances
easy_password = ""
hard_password = []

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!92
for i in range(num_letters):
    easy_password += random.choice(letters)
for i in range(num_symbols):
    easy_password += random.choice(symbols)
for i in range(num_numbers):
    easy_password += random.choice(numbers)

print("Easy version password: " + easy_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&p
for i in range(num_letters):
    hard_password.append(random.choice(letters))
for i in range(num_symbols):
    hard_password.append(random.choice(symbols))
for i in range(num_numbers):
    hard_password.append(random.choice(numbers))

random.shuffle(hard_password)
hard_password = "".join(hard_password)

print("Hard version password: " + hard_password)

