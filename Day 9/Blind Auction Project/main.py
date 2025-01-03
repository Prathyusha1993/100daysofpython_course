# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)

def find_highest_bidder(bids_dictionary):
    winner = ''
    highest_bid = 0

    # two ways to find max amount one using max funciton and other using for loop
    # winner = max(bids_dictionary, key=bids_dictionary.get)
    for bidder in bids_dictionary:
        bid_amount = bids_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f'The winner is {winner} with bid of ${highest_bid}')
    # print(f'The winner is {winner} with bid of ${bids_dictionary[winner]}')


should_continue = True
bids_dictionary = {}
while should_continue:
    user = input('What is your name?: ')
    amount = int(input('What is your bid? $'))
    bids_dictionary[user] = amount

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n ").lower()
    if more_bidders == 'no':
        should_continue = False
        find_highest_bidder(bids_dictionary)
    elif more_bidders == 'yes':
        print('\n' * 10)


