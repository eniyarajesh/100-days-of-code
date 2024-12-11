import random

word_list = ["apple","balloon","camel"]

lives = 6

print("Welcome to Hangman out!!")
chosen_word = random.choice(word_list)
print(chosen_word)
hangman = [
    " ___________",
    "|     |",
    "|    ( )",
    "|    \|/",
    "|     |",
    "|    / \ ",
    "|",
]
string1 = ""
for i in range(len(chosen_word)):
    string1 += "_"
print(string1)
print("")

game_over = False
correct_letter = []
while not game_over :
    string = ""
    guess = input("Enter a letter: ")
    for i in chosen_word:
        if guess == i:

            string += guess
            correct_letter.append(guess)
        elif i in correct_letter:
            string += i
        else:
            string += "_"
    print(string)
    print("")

    if guess not in chosen_word:
        lives -= 1
        print(f"Available lives: {lives}")
        if lives == 0:
            print("You lose")
            print("\n".join(hangman))
            game_over = True

    if "_" not in string:
        game_over = True
        print("You'r win!!")
    
    
