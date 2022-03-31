def my_function(*args, **kwargs):
    summa = 0
    for arg in args:
        try:
            if (type(arg) is int):
                summa += arg
        except:
            print("Not integer")
    return summa


def recursive_function(n):
    if n <= 1:
        return n
    else:
        return n + recursive_function(n - 1)


def recursive_even(n):
    if n == 0:
        return 0
    if not n % 2 == 0:
        return recursive_even(n - 1)
    else:
        return n + recursive_even(n - 1)


def recursive_odd(n):
    if n <= 1:
        return n
    if n % 2 == 0:
        return recursive_odd(n - 1)
    else:
        return n + recursive_odd(n - 1)


def keyboard():
    value = input("Please enter something:\n")
    if value.isnumeric():
        return value
    else:
        return 0


if __name__ == '__main__':
    print("Primul exemplu: ")
    print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
    print("Al doilea exemplu: ")
    print(my_function())
    print("Al treilea exemplu: ")
    print(my_function(2, 4, 'abc', param_1=2))
    print(recursive_function(6))
    print(recursive_even(6))
    print(recursive_odd(6))
    print(keyboard())
