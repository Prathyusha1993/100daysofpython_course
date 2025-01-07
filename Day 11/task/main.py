import random
from art import logo


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
    total = sum(cards)
    return total


def compare(u_score, c_score):
    if u_score == c_score:
        return 'Draw'
    elif c_score == 0:
        return 'User Lose'
    elif u_score == 0:
        return 'User Wins!'
    elif u_score > 21:
        return 'User lose'
    elif c_score > 21:
        return 'Computer lose'
    elif u_score > c_score:
        return 'User wins!'
    else:
        return 'You lose'


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to draw another card, or 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score:{computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play Blackjack game? Type 'y' or 'n': ").lower() == 'y':
    print('\n' * 20)
    play_game()

