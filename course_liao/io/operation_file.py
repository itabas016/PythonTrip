# -*- coding: utf-8 -*-

import os

print(os.path.abspath('.'))

with open('test.log', 'r') as f:
    print(f.read())


from io import StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World!')

print(f.getvalue())

from io import BytesIO
f = BytesIO()
f.write('这是中文'.encode('utf-8'))

print(f.getvalue())