import random
import os

clear = lambda: os.system('cls')
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You Lose"

    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose"
    elif user_score == 0:
        return "You Win"
    elif user_score > 21:
        return "You went over, you lose."
    elif computer_score > 21:
        return "Opponent went over, you win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, score: {user_score}")
        print(f"Computer cards: {computer_cards}, score: {computer_score }")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input("Type \'y\' to get another card, type \'n\' to pass: " ).lower() == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score=user_score, computer_score=computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()