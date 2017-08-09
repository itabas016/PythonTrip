# -*- coding: utf-8 -*-

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f1 = lazy_sum(1,2,4,5,6)
f2 = lazy_sum(1,2,4,5,6)

print('f1 == f2', f1 == f2)
print('f1() == f2()', f1() == f2())


def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print('f1()=', f1())
print('f2()=', f2())
print('f3()=', f3())

def count2():
    def f(j):
        def g():
            return j * j
        return g

    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f4, f5, f6 = count2()

print('f4()=', f4())
print('f5()=', f5())
print('f6()=', f6())

def count3():
    fs = []
    for i in range(1,4):
        fs.append((lambda j=i: j*j)(i))
    return fs

print('f7()=', count3())