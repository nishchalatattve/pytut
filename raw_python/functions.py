def my_func(cat="peter", *args, **kwargs):
    print(args)
    print(kwargs)


my_func("mike", 1, 2, 4, 5, sexy="99")