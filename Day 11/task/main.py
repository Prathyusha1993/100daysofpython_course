import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take alist of cards and return the score calculated from the cards"""
    total = sum(cards)
    if total == 21 and len(cards) == 2:
        return 0

    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)

    return total


def compare(u_score, c_score):
    if u_score == c_score:
        return 'Draw'
    elif c_score == 0:
        return 'Lose, opponent has Blackjack'
    elif u_score == 0:
        return 'Win with a BlackJack'
    elif u_score > 21:
        return 'You went over, you lose!'
    elif c_score > 21:
        return 'You win!'
    elif u_score > c_score:
        return 'You win'
    else:
        return 'you lose'

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"your final hand: {user_cards}, final_score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, computer_final_score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play blackjack game? Type 'y' or 'n': \n ").lower() == 'y'
    print('\n' * 20)
    play_game()









    # user_choice = input("Do you want to play blackjack game? Type 'y' or 'n': \n ")
    # if user_choice == 'y':
    #     print(logo)
    #     card1 = random.choice(cards)
    #     card2 = random.choice(cards)
    #     print(f'Your cards: [{card1}, {card2}], Current score: {card1 + card2}')
    #
    # computer_choice = random.choice(cards)
    # print(f"Computer's first choice is: {computer_choice}")
    # user_choice2 = input("Type 'y' to get another card, type 'n' to pass: ")
    # if user_choice2 == 'y':
    #     card3 = random.choice(cards)
    #     print(f"Your cards: [{card1}, {card2} , {card3}], Current Score: {card1+card2+card3}")
    # print(f"Computer's first choice is: {computer_choice}")

