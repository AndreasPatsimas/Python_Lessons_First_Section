def super_func(*args):  # this can accept any number of positional arguments like this
    return sum(args)


res = super_func(1, 2, 3)

print(res)


def my_super_func(*args, **kwargs):
    print(kwargs)
    # total = 0
    # for item in kwargs.values():
    #     total += item
    return max(args) + sum(kwargs.values())


super_result = my_super_func(3, 4, 5, x=1, y=2)

print(super_result)
