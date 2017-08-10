# -*- coding: utf-8 -*-

import pickle
import os
import sys

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

with open('%s\\dump.txt' % sys.path[0], 'wb') as f:
    pickle.dump(d, f)

with open('%s\\dump.txt' % sys.path[0], 'rb') as f:
    print(pickle.load(f))

print(os.getcwd())
print(sys.path[0])
