import random
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

num = random.randint(1,100)

def attempt_cal(attempts,n):
    while attempts != 0:
        print(f"You have {attempts} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        
        if guess == n:
            print("\n")
            print(f"Yay! You guessed the number correctly!!")
            return
        elif guess < n:
            print("Too low.")
            attempts -= 1
        elif guess > n:
            print("Too high.")
            attempts -= 1

        if guess != n and attempts > 1:
            print("Guess again")
        
    if attempts == 0 and guess != n:
        print("\n")
        print(f"Sorry, you ran out of attempts. The number was {n}.")

def num_guess(num):
    print(logo)
    print("Welcome to the Number Guessing Game!!")
    print("I'm thinking of a number between 1 and 100")
    print("If you guess the number correctly, you win!!")
    print("\n")

    level = input("Choose a difficulty. Type 'easy' or 'hard': " ).lower()
    if level == 'easy':
        attempt_cal(10,num)
    elif level == 'hard':
        attempt_cal(5,num)
    
num_guess(num)
