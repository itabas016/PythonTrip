# -*- coding: utf-8 -*-

def func1(a, b, c = 0, *args, **kw):
    print('a = ', a, 'b = ', b, 'c =', c, 'args = ', args, 'kw = ', kw)

def func2(a, b, c = 0, *, d, **kw):
    print('a = ', a, 'b = ', b, 'c =', c, 'd = ', d, 'kw = ', kw)

func1(1,2)
func1(1,2,3)
func1(1,2,3,'a','b')
func1(1,2,3,'a','b',('c','d'))
func1(1,2,3,'a','b',('c','d'),x=99)
func1(1,2,3,'a','b',('c','d'),x=99,y=100)
func1(1,2,3,'a','b',('c','d'),x=99,y=100,z={'m':1,'n':2})

args=(1,2,3,4)
kw={'p':2,'q':4}

func1(args,kw)
func1(*args,**kw)

args=(1,2,3)
kw={'d':9,'q':4}
func2(*args,**kw)