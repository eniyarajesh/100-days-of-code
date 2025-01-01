import random
from art import guess_number

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
    print(guess_number)
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