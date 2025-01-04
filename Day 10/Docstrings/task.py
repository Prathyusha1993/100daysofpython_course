def format_name(f_name, l_name):
    '''take a first and last name and format it to return the title case version of the name.'''

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)


# ghhjn
# kjiygbk
# yffxchb
# bkhgh

def my_function(a):
    if a < 40:
        return
        print('Terrible')
    if a < 80:
        return 'pass'
    else:
        return 'great'

print(my_function(25))