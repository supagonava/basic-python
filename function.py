def func_name(a, b):
    return a + b


def func_with_default_value(a=10, b=10):
    return a + b


def recursive_func(n=1):
    print("n=", n)
    if n < 10:
        n += 1
        return recursive_func(n)

    return n


print(func_name(10, 20))  # 30
print(func_with_default_value())  # 20
print(func_with_default_value(a=5, b=20))  # 25
recursive_func()
