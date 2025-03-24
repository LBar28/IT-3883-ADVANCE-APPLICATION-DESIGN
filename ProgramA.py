# Program Name: Assignment4:ProgramA.py 
# Course: IT3883/Section W02
# Student Name: Leonardo Barranco
# Assignment Number: Lab4
# Due Date: 3/24/2025
# Purpose: The program astableshes a network connection and program B can sent a string to program A which will print it out

import socket


def ProgramA():
    host = 'localhost'
    port = 45000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    message = input("Type a string to send: ")
    client.sendall(message.encode('utf-8'))

    response = client.recv(1024).decode('utf-8')
    print(f"Received message: {response}")

    client.close()

if __name__ == "__main__":
    ProgramA()
