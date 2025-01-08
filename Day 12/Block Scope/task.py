# there is no black scope in python

game_level = 3
enemies = ['skeleton', 'zombie', 'alien']

if game_level < 5:
    new_enemy = enemies[0]
print(new_enemy)

my_global_var = 1   #accessible naywhere

def my_function():
    my_local_Var = 2   #only access within function function scope or local scope

for _ in range(10):
    my_block_var = 3   #accessible anywhere



# prime number check:
def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(73))