# Program Name: Assignment4:ProgramB.py 
# Course: IT3883/Section W02
# Student Name: Leonardo Barranco
# Assignment Number: Lab4
# Due Date: 3/24/2025
# Purpose: The program estableshes a network connection and program B can sent a string to program A which will print it out
#https://www.geeksforgeeks.org/socket-programming-python/

import socket 

def ProgramB():
    host = 'localhost'
    port = 45000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"Listening on {host}:{port}...")

    conn, addr = server.accept()
    print(f"Connected to {addr}")
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data.upper())

    conn.close()
    server.close()

if __name__ == "__main__":
    ProgramB()
