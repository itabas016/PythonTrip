# -*- coding: utf-8 -*-

print([x * x for x in range(1,11)])
print([x * x for x in range(1,11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'abc'])

import os

print([d for d in os.listdir('.')])
print([d for d in os.listdir('../.')])
print([d for d in os.listdir('../../.')])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
print([s.upper() for s in L])


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)