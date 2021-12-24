def funl(a):
    x = a * 3

    def fun2(b):
        nonlocal x
        return b + x

    return fun2


