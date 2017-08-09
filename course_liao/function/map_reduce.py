# -*- coding: utf-8 -*-

def f(x):
    return x * x

a = [0,1,2,3,4,5,6,7,8,9]
b = range(10)

print(type(a))
print(type(b))

print(list(map(f, a)))
print(list(map(str, a)))

print(list(map(lambda x: x *x, a)))
print(list(map(lambda x: x *x, list(b))))

#reduce(f, [x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)

def g(x, y):
    return x+y

from functools import reduce
print(reduce(g, a))

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print(str2int('1234'))

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int_s(s):
    return lambda x, y: x*10 +y, map(char2num, s)

print(str2int_s('1234'))