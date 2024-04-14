# Edge Computing Project

This repository contains the resources and instructions for setting up an edge computing environment using Docker. The focus is on demonstrating basic Docker virtualization and Docker networking within the context of an educational project in the Advances in Wireless Networking module given by the School of Computer Science of University College Dublin.

## Project Overview

The project is structured to accomplish two primary tasks:
1. **Basic Docker Virtualization** - To setup and run various Docker images to demonstrate Docker capabilities.
2. **Docker Networking** - To establish and test connectivity and communication between Docker containers.

### Technologies Used
- Docker
- Ubuntu
- Python3

## Python Scripts Description

### Client File : `ipc_client_csv.py`

This Python script is designed to run within the client Docker container. It handles:
- Reading data from a specified CSV file.
- Connecting to the server using sockets.
- Sending CSV data to the server for processing.
- Optionally, it can receive and print responses from the server.

#### Functionality
- **Read CSV**: The script reads a CSV file to extract data that needs to be processed.
- **Socket Communication**: Establishes a socket connection with the server and sends data line by line.
- **Receive Responses**: Listens for responses from the server after sending data.

### Server File : `ipc_server_csv.py`

This script runs within the server Docker container and is responsible for:
- Receiving data sent by the client over a socket connection.
- Processing the data, which could involve calculations or database operations.
- Sending back responses to the client after processing.

#### Functionality
- **Receive Data**: Listens on a socket for incoming data from the client.
- **Process Data**: Performs necessary operations on the received data.
- **Send Response**: Sends a processed response back to the client.
- 
### Prerequisites

Ensure Docker is installed on your system. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).

#### Clone the Repository

Start by cloning this repository to get all the necessary project files.

```bash
git clone https://github.com/xXMagIkZzR4mBOXx/EdgeComputing_Project.git
cd EdgeComputing_Project
```
## Dockerfile Descriptions

### Client Dockerfile

The `Dockerfile_client` sets up an environment for running a Python-based client application. It includes:
- Base image from Ubuntu with Python installed.
- Copies a Python script (`ipc_client.py`) into the container.
- Executes the client script when the container starts.

#### Building and Running the Server Container

To build and run the Docker container for the client:

```bash
cd path_to_Dockerfile_client #replace by your path
docker build -f Dockerfile_server_csv .
docker run --name client_container Dockerfile_server_csv
```
#### Building and Running the Client Container

To build and run the Docker container for the client:

```bash
cd path_to_Dockerfile_client #replace by your path
docker build -f Dockerfile_client_csv .
docker run --name client_container Dockerfile_client_csv
```
#### Building an IPC Network and Offloading Data from Server to Client
After having built both Server and Client containers, and given the associated Python scripts, use these commands :

```bash
docker network create ipc_network
docker run --network ipc_network --name server -d ipc-server # runs in detached mode --> logs invisible
docker run --network ipc_network --name client -d ipc-client # runs in detached mode --> logs invisible
```
To get the logs of both Client and Server containers, you can then use these commands :

```bash
docker logs server
docker logs client
```
