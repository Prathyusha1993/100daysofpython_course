def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    # print(f'{formatted_f_name} {formatted_l_name}')
    return f'{formatted_f_name} {formatted_l_name}'

print(format_name('prathyusha', 'kurigala'))


def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_1('hello')
print(output)
print(function_2(output))
