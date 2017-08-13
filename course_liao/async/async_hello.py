#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import threading

@asyncio.coroutine
def hello():
    print('Hello world!')
    r = yield from asyncio.sleep(1)
    print('Hello again')


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()

@asyncio.coroutine
def hello_thread():
    print('Hello world! (%s)' % threading.current_thread())
    yield from asyncio.sleep(1)
    print('Hello again (%s)' % threading.current_thread())

loop2 = asyncio.get_event_loop()
tasks = [hello_thread(), hello_thread()]
loop2.run_until_complete(asyncio.wait(tasks))
loop2.close()


async def hello2():
    print('Hello world!')
    r = await asyncio.sleep(1)
    print('Hello again')

loop3 = asyncio.get_event_loop()
tasks3 = [hello2(), hello2()]
loop3.run_until_complete(asyncio.wait(tasks3))
loop3.close()