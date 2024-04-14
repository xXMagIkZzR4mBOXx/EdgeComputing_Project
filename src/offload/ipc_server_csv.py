#!/usr/bin/env python3
# ipc_server.py

import socket
import numpy as np  # Import numpy for numerical operations

HOST = '0.0.0.0'
PORT = 9898        # Port to listen on (non-privileged ports are > 1023)

# Function to compute the mean of received data
def compute_mean(data_list):
    data_array = np.array(data_list, dtype=float)  # Convert list to numpy array of type float
    return np.mean(data_array)

# Main server loop
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        received_data = []

        while True:
            data = conn.recv(1024).decode('utf-8')  # Decode the incoming data
            if not data:
                break  # If no data is received, exit the loop
            if data == 'calculate':
                # Calculate the mean if 'calculate' command is received
                mean_value = compute_mean(received_data)
                conn.sendall(f"Mean: {mean_value}".encode('utf-8'))
                received_data.clear()  # Optionally clear the list after calculation
            else:
                try:
                    # Try converting received data to float and store it
                    received_data.append(float(data))
                except ValueError:
                    # Send an error message if conversion fails
                    conn.sendall(b"Error: Invalid numeric data.")
                else:
                    # Acknowledge the data receipt
                    conn.sendall(b"Data received.")