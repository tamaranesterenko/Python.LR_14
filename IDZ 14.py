# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import sys


def fun1(to_replace, replacer):

    def fun2(string):
        nonlocal to_replace, replacer
        result = string.replace(replacer, to_replace)
        return result

    return fun2


if __name__ == "__main__":
    x = str(input("Введите строку: "))
    c = str(input("Введите символ, который нужно заменить: "))
    h = str(input("Введите символ, на который заменить: "))
    rep = fun1(h, c)
    print(rep(x))
