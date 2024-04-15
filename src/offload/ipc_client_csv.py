#!/usr/bin/env python3
# ipc_client.py

import socket
import pandas as pd

HOST = 'server' 
PORT = 9898        
CSV_FILE = 'data.csv' 
COLUMN_NAME = 'marks' 

def read_column(file_path, column_name):
    df = pd.read_csv(file_path, delimiter=';')  
    print(f"Columns found in CSV: {df.columns.tolist()}") 
    if column_name in df.columns:
        return df[column_name].astype(str).tolist()
    else:
        raise ValueError(f"Column {column_name} does not exist in the file. Available columns: {df.columns.tolist()}")

def send_data_to_server(host, port, data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        for item in data:
            s.sendall(item.encode('utf-8'))
            response = s.recv(1024) 
            print('Server response:', response.decode('utf-8'))
        
        s.sendall('calculate'.encode('utf-8'))
        final_response = s.recv(1024)
        print('Final response:', final_response.decode('utf-8'))

if __name__ == '__main__':
    try:
        column_data = read_column(CSV_FILE, COLUMN_NAME)
        send_data_to_server(HOST, PORT, column_data)
        print('Data sent and mean calculated.')
    except ValueError as e:
        print(e)
