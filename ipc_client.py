#!/usr/bin/env python3
# ipc_client.py

import socket

HOST = 'server'
PORT = 9898 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world. IPC success!')
    data = s.recv(1024)

print('Received', repr(data))
