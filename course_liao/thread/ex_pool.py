#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os, time, random


def long_time_task2(name):
    i = 0
    while i<=50000000:
        i = i+1
        i = i-1
        i = i+1
        i = i+0

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(10)
    end = time.time()
    print('Task %s run %0.2f seconds.' % (name, (end-start)))

if __name__ == '__main__':
    start = time.time()
    
    print('Parent process %s.' % os.getpid())
    p = Pool(3)
    for i in range(3):
        p.apply_async(long_time_task2, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

    end = time.time()
    print('Task run %0.2f seconds.' % ((end-start)))