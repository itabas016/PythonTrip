#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 12345))

print(s.recv(1024).decode('utf-8'))

for data in input_list:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()