# -*- coding: utf-8 -*-

import os
import sys

print(os.path.abspath('.'))

with open('%s\\text.log' % sys.path[0], 'r') as f:
    print(f.read())

with open('%s\\text.log' % sys.path[0], 'w') as f:
    print(f.write("Insert a new line for test"))
    print(f.write("\r\n测试插入一行中文"))


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


print([x for x in os.listdir(sys.path[0])])
print([x for x in os.listdir(sys.path[0]) if x.split('.')[1] == 'py'])
print([x for x in os.listdir(sys.path[0]) if x[-2:] == 'py'])
print([x for x in os.listdir(sys.path[0]) if os.path.splitext(x)[1] == '.py'])
