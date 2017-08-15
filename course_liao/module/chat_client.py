#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, threading, time, sys, os

HOST = '127.0.0.1'
PORT = 12345
BUFFER_SIZE = 1024
UTF8 = 'utf-8'
COMMAND_EXIT = 'exit'

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
c.connect((HOST, PORT))

while True:
    print('Client process Id: %s' % os.getpid())
    print(c.recv(BUFFER_SIZE).decode(UTF8))
    # c.send((sys.argv).encode())
    c.send('Hello server'.encode(UTF8))
    print(c.recv(BUFFER_SIZE).decode(UTF8))
    time.sleep(5)

c.send(b'exit')
c.close()