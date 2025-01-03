programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": 'An action doing something in loop over and over again.'
}

print(programming_dictionary['Bug'])
print(programming_dictionary['Function'])

# adding new key value pair to dictionary
programming_dictionary['List'] = 'Contains a list of element in an array is called as list in python.'
print(programming_dictionary)
print(programming_dictionary['List'])

# modifying the key value in dictionary
programming_dictionary['Function'] = "A piece of code that you can easily call over and over again in python."
print(programming_dictionary['Function'])

empty_dictionary = {}
empty_dictionary['Apple'] = 'Red'
empty_dictionary['Pear'] = 'Green'
empty_dictionary['Banana'] = 'Yellow'
print(empty_dictionary)
# edit
empty_dictionary['Apple'] = 'Green'
print(empty_dictionary)

# add
empty_dictionary['Peach'] = 'Pink'
print(empty_dictionary)

# loop through a dictionary and print keys:
for key in empty_dictionary:
    print(key)

# loop through a dictionary for values:
for thing in empty_dictionary:
    print(f'{thing} - {empty_dictionary[thing]}')