# -*- coding: utf-8 -*-

# n! = 1 * 2 * 3 * 4 * 5 ... * n
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

fact(1)
fact(4)
fact(10)

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

fact_iter(10,1)

# Hanronic
def move(n, a, b, c):
    if n == 1:
        print(a, ' --> ', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(3,'A','B','C')