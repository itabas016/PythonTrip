# -*- coding: utf-8 -*-

L=[]
n=1
while n < 100:
    L.append(n)
    n+=2

print(L)
print(list(range(1,100,2)))

L=list(range(1,100,2))
H=L[0:int(len(L)/2)]
print(H)

L=list(range(100))
print(L[:10])
print(L[-10:])

print(L[:20:3])
print(L[::5])

J=L[:]
print(J)

t=(0,1,2,3,4,5)[:]
print(t)
t=(0,1,2,3,4,5)[:3]
print(t)

s='ABCDEFGHIJKL'
print(s[:3])
print(s[::3])

L=list(range(10))
L[::2]= [-i for i in L[::2]]
print(L, 'with len = ', len(L))