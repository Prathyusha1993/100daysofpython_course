# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


a= 1
def my_func():
    global a
    a += 1
    print(a)

my_func()