# Functions with input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

# function with multiple inputs positional arguments:
def greet_with_multiple(name, location):
    print(f'Hello {name}')
    print(f'what is famous in your {location}')

greet_with_multiple('Pinky', 'USA')
greet_with_multiple('USA', 'Pinky')

# keyword arguments:
greet_with_multiple(location = 'USA', name ='Pinky')

# example for keyword arguments:
def my_func(a, b, c):
    print(a,b,c)
my_func(1,2,3)
my_func(c=3, a=1,b=2)