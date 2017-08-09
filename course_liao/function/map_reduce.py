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

