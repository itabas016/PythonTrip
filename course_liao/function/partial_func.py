# -*- coding: utf-8 -*-

print(type(int(123)))
print(int(123))

print(type(int('1234')))
print(int('1234'))

import functools
print(int('1000110', base=2))
print(functools.partial(int, base=2)('1000110'))
print(functools.partial(int, base=2)('1000110', base=10))