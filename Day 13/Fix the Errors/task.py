try:
    age = int(input('How old are you?'))
except ValueError:
    print('You have typed invalid number,please try again with numerical number')
    age = int(input('How old are you?'))
if age > 18:
    print(f'you can drive at {age}')