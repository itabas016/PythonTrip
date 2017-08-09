# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1,2,3,4,5,6,8])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', 'sa', '', '1223', None, 'D'])))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0