from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(ingredients):
    '''returns true when order can be made and false if ingredients are sufficient'''
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    '''total calculated couns inserted'''
    input('Please insert the coins:')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.10
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    '''return true if money is sufficient is accepted or false if money is insufficient'''
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print('Sorry thats not enough money.Money refunded.')
        return False


def make_coffee(drink_name, order_ingredients):
    '''deduct the required ingredients from resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕️')



print(logo)
print(f"Report: Water: {resources['water']}ml \n Milk:{resources['milk']}ml \n Coffee: {resources['coffee']}g")

should_continue = True

while should_continue:
    choose = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choose == 'off':
        should_continue = False
    elif choose == 'report':
        print(f"Report: Water: {resources['water']}ml \n Milk:{resources['milk']}ml \n Coffee: {resources['coffee']}g \n Money: {profit}$")
    else:
        drink = MENU[choose]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choose, drink['ingredients'])



