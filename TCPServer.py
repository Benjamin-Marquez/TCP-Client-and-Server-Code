from socket import *
import os

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',12000))

# Listening For Connections
serverSocket.listen(1)
print("The server is ready to receive... \n")

while(True):
    # Create Connection Socket
    connectionSocket, address = serverSocket.accept()
    
    incomingMessage = connectionSocket.recv(2048)
    print("HTTP request:")
    print(incomingMessage.decode())

    # Parsing Through the Incoming Message 
    message = incomingMessage.decode()
    messageList = message.split(' ')
    # Checking if its the correct file based of location in the message list created by the .split
    if messageList[1] == ("/index.html"):
        print("Object to be fetched: {}".format("index.html"))
        print("Object Content:")
        # Opening and Reading the file
        f = open("index.html")
        read = f.read()
        print(read + "\n")
        
        print("HTTP response message:\nHTTP/1.1 200 OK\n")

        print(read + "\n")
        # Storing the new message to later be sent
        modifiedMessage = ("HTTP/1.1 200 OK\n\n" + read)
    else:
        newList = messageList[1].split('/')
        print("Object to be fetched: {}\nHTTP response message:\nHTTP/1.1 404 Not Found".format(newList[1]))
        modifiedMessage = ("HTTP/1.1 404 Not Found")

    connectionSocket.send(modifiedMessage.encode())

    connectionSocket.close()
    
