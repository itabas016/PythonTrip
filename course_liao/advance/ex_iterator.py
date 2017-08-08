# -*- coding: utf-8 -*-

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key,d[key])

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)

from collections import Iterable

isinstance('abcdef', Iterable)
isinstance((1,2,3,4), Iterable)
isinstance(1234, Iterable)

l = ['A','B','C','D']
print('enumerate for ', l)
for i, value in enumerate(l):
    print(i, value)

l = 'abcde'
print('enumerate for ', l, ': ')
for i, value in enumerate(l):
    print(i, value)