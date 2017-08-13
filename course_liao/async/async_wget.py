#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

print('Execute wget function:')
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.baidu.com', 'www.yahoo.com', 'www.sohu.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

def wget2(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


print('Execute wget2 function use await features:')
loop2 = asyncio.get_event_loop()
tasks2 = [wget(host) for host in ['www.baidu.com', 'www.yahoo.com', 'www.sohu.com']]
loop2.run_until_complete(asyncio.wait(tasks2))
loop2.close()