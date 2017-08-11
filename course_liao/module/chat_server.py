#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, threading, time, os

HOST = '127.0.0.1'
PORT = 12345
MAX_CONNECTION = 5
BUFFER_SIZE = 1024
UTF8 = 'utf-8'
COMMAND_EXIT = 'exit'


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(MAX_CONNECTION)
print('Server process Id: %s' % os.getpid())


while True:
    print('Waiting for connection...')
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

def tcplink(sock, addr):
    print('Accept new connect from %s %s...' % (sock, addr))
    print('Server subprocess Id: %s' % os.getpid())
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(BUFFER_SIZE)
        time.sleep(1)
        if not data or data.decode(UTF8) == COMMAND_EXIT:
            break
        sock.send(('Hello, %s!' % data.decode(UTF8)).encode(UTF8))
    sock.close()
    print('Connection from %s:%s closed.' % addr)