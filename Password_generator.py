import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '<', '>', '?', '|', '~']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
req_letter = int(input("How many letters would you like in your password?\n"))
req_symbols = int(input("How many letters would you like?\n"))
req_number = int(input("How many letters would you like?\n"))

password = []

#generate letters
for i in range(req_letter):
    password.append(random.choice(letters))
           
#generate symbols
for i in range(req_symbols):
    password.append(random.choice(symbols))

#generate number
for i in range(req_number):
    password.append(random.choice(number))

#shuffle pswd
random.shuffle(password)

for pswd in password:
    print(pswd,end="")

    
