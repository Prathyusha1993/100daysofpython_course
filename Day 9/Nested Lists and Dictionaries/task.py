
capitals = {
    'France': 'Paris',
    'Germany': 'Berlin'
}

# nested list in dictionary:
travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Stuttgart', 'Berlin']
}
print(travel_log['France'][1])
print(travel_log['Germany'][0])

# editing value to germany
travel_log['Germany'][1] = 'Hamburg'
print(travel_log)

# nested list
nested_list = ['A', 'B', ['C','D']]
print(nested_list[2][1])

# nesting a dictionary inside a dictionary:
travel_log_dictionary = {
    'France': {
        'total_visits': 2,
        'cities_visited': ['Paris', 'Lille','Dijon']
    },
    'Germany': {
        'cities_visited': ['Stuttgart', 'Berlin', 'Hamburg'],
        'total_visits': 5
    }
}
print(travel_log_dictionary['Germany']['cities_visited'][0])

# another example using dictionaries:
starting_dictionary = {
    'a': 9,
    'b': 8
}
final_dictionary = {}
starting_dictionary['c'] = 7
final_dictionary = starting_dictionary
print(final_dictionary)

# example
dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}
for key in dict:
    dict[key] += 1
    print(dict[key])

#  ex
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order['main'][2][0])
