print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input('What is your age?: '))
    if age <= 12:
        bill = 5
        print('Child tickets are $5')
    elif age <= 18:
        bill = 7
        print('Youth tickets are $7')
    else:
        bill = 12
        print('adult tickets are $12')
    want_photos = input("Do you want to take photos? (y/n): ")
    if want_photos == 'y':
        bill += 3

    print(f'total bill is ${bill}')
else:
    print("Sorry you have to grow taller before you can ride.")


# another example
math_score = 93
english_score = 95
if math_score >= 90:
    if english_score >= 90:
        print('You are good at everything')
    else:
        print('you are good at maths')
if english_score >= 90:
    print('you are good at english')

