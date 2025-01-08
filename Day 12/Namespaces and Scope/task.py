enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

def testing_global_scope():
    print(f"enemies outside function: {enemies}")

testing_global_scope()

# local scope or function scope
def drink_potion():
    potion_strength = 2
    print(f" {potion_strength}")

drink_potion()
# print(potion_strength)  name error

# global scope
player_health = 10
def check_player_health():
    print(player_health)
check_player_health()

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()
game()