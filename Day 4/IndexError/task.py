states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)
print(len(states_of_america))
# print(states_of_america[50]) index error list out of range

# nested lists or 2d lists:
# dirty_dozens = ['strawberries', 'Spinach', 'kale', 'Apples', 'Grapes', 'Nectarines']
fruits = ['cherry', 'apples', 'grapes', 'strawberries']
veggies = ['Spinach', 'kale', 'tomatoes', 'celery']
dirty_dozen = [fruits, veggies]
print(dirty_dozen)
print(dirty_dozen[0][0])
print(dirty_dozen[0][1])
print(dirty_dozen[1][1])
print(dirty_dozen[1][3])