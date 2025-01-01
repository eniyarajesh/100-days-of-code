import random
from game_data import data
from art import logo, vs

def account_details(account):   
        account_name = account["name"]
        account_description = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_description}, from {account_country}."

def correct_answer(count_a, count_b):
    if count_a["follower_count"] > count_b["follower_count"]:
        return "A"
    else:
        return "B"

def start_game(logo):
    game_continue = True
    score = 0
    while game_continue:
        choice_a = random.choice(data)
        choice_b = random.choice(data)
        if choice_a["name"] == choice_b["name"]:
            choice_b = random.choice(data)

        print(f"Compare A: {account_details(choice_a)}")
        print(vs)
        print(f"Against B: {account_details(choice_b)}")
        
        # guess who has more followers
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # check player guess is correct or not 
        crct_ans = correct_answer(choice_a, choice_b)
        
        # print the player score
        if guess == crct_ans:
            score += 1
            print("\n" * 10)
            print(logo)
            print(f"You're right! Current score: {score}")
            print("\n")
            
        else:
            print("\n")
            print(f"Sorry, that's wrong. Final score: {score}")
            game_continue = False

# ask whether player wants to continue the game
while input("Do you want to play Higher Lower Game!. Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)
    print(logo)
    start_game(logo)