import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def choose_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def cal_score(score):
    if sum(score) == 21 and len(score) == 2:
        return 0
    elif 11 in score and sum(score) > 21:
        score.remove(11)
        score.append(1) 

    return sum(score)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    
def play_game():
    print(logo)
    user_card = []
    computer_card = []
    user_score = 0
    computer_score = 0

    for i in range(2):
        user_card.append(choose_card())
        computer_card.append(choose_card())

    game_over = False
    while not game_over:
        user_score = cal_score(user_card)
        computer_score = cal_score(computer_card)

        print(f"Your card: {user_card}, score = {user_score}") 
        print("Computer first card: ", computer_card[0])

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else: 
            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choice == 'y':
                user_card.append(choose_card())
                user_score = cal_score(user_card)
            else:
                game_over = True
        
    while computer_score != 0 and computer_score < 17:
        computer_card.append(choose_card())
        computer_score = cal_score(computer_card)

    print("\n")   
    print(f"Your final card: {user_card}, score = {user_score}") 
    print(f"Computer's final card: {computer_card}, score: {computer_score}")
    print(compare(user_score, computer_score))
          
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()


