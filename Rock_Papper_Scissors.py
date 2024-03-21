import random

rule=["rock","papper","scissor"]

print("type '0' for rock, type '1' for papper, type '1' for scissor ")
user_choice=int(input())

random_choice=len(rule)
random_choice=random.randint(0,random_choice - 1)

print("YOUR CHOICE IS :", user_choice)
print("BOT CHOICE IS :", random_choice)


if ((user_choice == 0) and (random_choice == 1)) or ((user_choice == 0) and (random_choice == 2)):
    print("You lose")
elif (user_choice == 1) and (random_choice == 0) or ((user_choice == 2) and (random_choice == 1)):
    print("You win")
