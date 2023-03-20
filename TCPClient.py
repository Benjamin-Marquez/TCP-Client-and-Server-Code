from socket import * 
import sys 

# Create Client Socket 
clientSocket = socket(AF_INET, SOCK_STREAM)

# Cmd Line Arguments 
ipAddress = sys.argv[1]
serverPort = int(sys.argv[2])
requestedObject = sys.argv[3]

# Get IP Address
serverAddress = (ipAddress, serverPort)
# Connect to Server
clientSocket.connect(serverAddress)

# HTTP GET Request
print("HTTP request to server:")
request = ("GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n".format(requestedObject, ipAddress))
clientSocket.send(request.encode())
print("GET /" + requestedObject + " HTTP/1.1")
print("Host: {}".format(ipAddress))

# Receive Server's Response
receivedMessage = clientSocket.recv(2048)
print("\nHTTP response from server:\n" + receivedMessage.decode())

# Close Client Socket 
clientSocket.close()
