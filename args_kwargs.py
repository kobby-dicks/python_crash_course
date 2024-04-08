def Number_of_fruits(*args, **kwargs,):
    print(args, type(args))
    print(kwargs, type(kwargs))


def add(x, *any_number):
    for num in any_number:
        x += num
        print(x)