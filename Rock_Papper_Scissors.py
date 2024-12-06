import random
rule=["rock","papper","scissor"]

print("type '0' for rock, type '1' for papper, type '2' for scissor ")
user_choice=int(input())

rule_length = len(rule)-1
random_choice = random.randint(0,rule_length)

print("YOUR CHOICE IS :", user_choice)
print("BOT CHOICE IS :", random_choice)

if user_choice > rule_length:
    print("Invalid Number!! \n You lose")
elif user_choice == random_choice:
    print("It's a draw!!")
elif ((user_choice == 0) and (random_choice == 2)) or ((user_choice == 1) and (random_choice == 0)) or ((user_choice == 2) and (random_choice == 1)):
    print("You win!!")
elif ((user_choice == 0) and (random_choice == 1)) or ((user_choice == 1) and (random_choice == 2)) or ((user_choice == 2) and (random_choice == 0)):
    print("You lose")
