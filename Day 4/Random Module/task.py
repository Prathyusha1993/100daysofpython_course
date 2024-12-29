import random
import my_module

numbers = random.randint(1, 10)
print(numbers)

print(my_module.my_fav_numb)

# random floating point numbers
float_nums = random.random()
print(float_nums)

# expand the range of floating point num by multiplication
float_nums = random.random() * 10
print(float_nums)

# another way to generate random floating point num
float_numb = random.uniform(1, 10)
print(float_numb)

# choice
choice = random.choice([12,13,14,15])
print(choice)


# example
coin = random.choice(['Heads', 'Coins'])
print(coin)

random_heads_tails = random.randint(0, 1)
if random_heads_tails == 0:
    print('Heads')
else:
    print('Tails')