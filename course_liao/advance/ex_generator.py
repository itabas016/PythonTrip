# -*- coding: utf-8 -*-

L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(next(g))

for n in g:
    print(n)


def fib(max):
    n,a,b = 0,0,1
    print('Normally, fib for', max, ': ')
    while n < max:
        print(b)
        a, b = b, b+a
        n = n+1
    return 'done'

fib(5)

def g_fib(max):
    n,a,b = 0,0,1
    print('By generator, fib for', max, ': ')
    while n < max:
        yield b
        a, b = b, b+a
        n = n+1
    return 'done'

g_fib(5)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o=odd()
print('output odd numbers: ')
for g in o:
    print(g)

# print a graph for triangles
def triangles():
    L = [1]
    i = 0

    while i<6:
        i = i+1
        yield print(L)
        L.append(1)
        L = [L[j]+L[j-1] for j in range(0,len(L))]

for x in triangles():
    pass