#!/usr/bin/python3 python
# -*- coding: utf-8 -*-

import asyncio
import os, sys
from datetime import datetime

from aiohttp import web
import aiofiles

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Hello World</h1>', content_type='text/html')

async def timestamp(request):
    t = datetime.now().timestamp()
    # with open('/var/www/test/data/%s.log' % t, 'w') as f:
    # async with aiofiles.open('%s\data\%s.log' % (sys.path[0], t), 'w') as f:
    async with aiofiles.open('%s\data\%s.txt' % (sys.path[0], request.match_info['id']), 'w') as f:
        # await f.write(str(t))
        async with aiofiles.open('%s\test.xml' % sys.path[0], 'r') as rf:
            x = await rf.read()
        await f.write(str(x))
    # with open('/var/www/test/data/%s.log' % t, 'r') as f:
    # async with aiofiles.open('%s\data\%s.log' % (sys.path[0], t), 'r') as f:
    async with aiofiles.open('%s\data\%s.txt' % (sys.path[0], n), 'r') as f:
        text = '<h1> timestamp: %s </h1>' % await f.read()
        return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/timestamp', timestamp)
    app.router.add_route('GET', '/timestamp/{id}', timestamp)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    print('Server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
