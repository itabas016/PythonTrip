# -*- coding: utf-8 -*-

from datetime import datetime

def now():
    print(datetime.now())

print(now())

def log(func):
    def wrapper(*args, **kw):
        print('call this method %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now2():
    print(datetime.now())

print(now2())

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now3():
    print(datetime.now())

print(now3())