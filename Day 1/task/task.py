print('Hello, Welcome to the band name generator!')
city = input('Enter the city name that you grew up?\n')
pet_name = input('Enter your pet name?\n')
print(f'Your band name is {city} {pet_name}')

# example:
print('Welcome to the tip calculator!')
bill = float(input('What was the total bill?\n'))
tip = float(input('How much tip would you like to give? 10, 12, or 15?\n'))
split = float(input('How many people to split bill?\n'))
print(f'Each person should pay: {(bill+tip)/split}')