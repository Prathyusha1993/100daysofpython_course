def format_name(f_name, l_name):
    if f_name == '' or l_name == '':
        return 'You did not provide valid inputs'
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


# print(format_name("praThyUsha", "kuriGala"))
print(format_name(input('What is your firstname?'), input('What is your lastname? ')))

