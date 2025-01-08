import random
import art
from game_data import data

def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"

# print(format_data(random.choice(data)))

def check_answer(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

# print(check_answer('b', 56, 90))

print(art.logo)
score = 0
should_continue = True
output_b = random.choice(data)

while should_continue:
    output_a = output_b
    output_b = random.choice(data)

    if output_a == output_b:
        output_b = random.choice(data)

    print(f"Compare A: {format_data(output_a)}.")
    print(art.vs)
    print(f"Against B: {format_data(output_b)}.")

    guess = input("Who has more followers.Type 'A' or 'B': ").lower()

    a_follower_count = output_a['follower_count']
    b_follower_count = output_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"Your Right. Current score: {score}")
    else:
        print(f"Sorry. Wrong answer. final score:{score}")
        should_continue = False

