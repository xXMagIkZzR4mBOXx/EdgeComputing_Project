#!/usr/bin/env python3
# ipc_client.py

import socket
import pandas as pd

HOST = 'server'  # The server's hostname or IP address
PORT = 9898         # The port used by the server
CSV_FILE = 'data.csv'  # Path to your CSV file
COLUMN_NAME = 'marks'  # Name of the column to send

def read_column(file_path, column_name):
    df = pd.read_csv(file_path, delimiter=';')  # Specify the delimiter used in your CSV file
    print(f"Columns found in CSV: {df.columns.tolist()}")  # Debug: print the columns in the CSV
    if column_name in df.columns:
        return df[column_name].astype(str).tolist()
    else:
        raise ValueError(f"Column {column_name} does not exist in the file. Available columns: {df.columns.tolist()}")

# Connect to the server and send data
def send_data_to_server(host, port, data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        for item in data:
            s.sendall(item.encode('utf-8'))
            response = s.recv(1024)  # Optionally receive a response from the server for each item
            print('Server response:', response.decode('utf-8'))
        
        # After sending all data, send the 'calculate' command
        s.sendall('calculate'.encode('utf-8'))
        final_response = s.recv(1024)
        print('Final response:', final_response.decode('utf-8'))

# Main execution
if __name__ == '__main__':
    try:
        column_data = read_column(CSV_FILE, COLUMN_NAME)
        send_data_to_server(HOST, PORT, column_data)
        print('Data sent and mean calculated.')
    except ValueError as e:
        print(e)  # Print the error message if the column is not found
