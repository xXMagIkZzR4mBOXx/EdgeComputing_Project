#!/usr/bin/env python3
# ipc_server.py

import socket
import numpy as np 

HOST = '0.0.0.0'
PORT = 9898  

def compute_mean(data_list):
    data_array = np.array(data_list, dtype=float)
    return np.mean(data_array)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        received_data = []

        while True:
            data = conn.recv(1024).decode('utf-8') 
            if not data:
                break 
            if data == 'calculate':
                mean_value = compute_mean(received_data)
                conn.sendall(f"Mean: {mean_value}".encode('utf-8'))
                received_data.clear() 
            else:
                try:
                    received_data.append(float(data))
                except ValueError:
                    conn.sendall(b"Error: Invalid numeric data.")
                else:
                    conn.sendall(b"Data received.")
