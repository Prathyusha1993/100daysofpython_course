import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))

# other option
random_index = random.randint(0, 4)
print(friends[random_index])

