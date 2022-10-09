#import socket module
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
    try:
        message = connectionSocket.recv(1024).decode()#Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()#Fill in start #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        #https://stackoverflow.com/questions/40320591/python-web-server-socket
        connectionSocket.send(bytes('\nHTTP/1.1 200 OK\n\n','UTF-8'))
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            #https://stackoverflow.com/questions/40320591/python-web-server-socket
            connectionSocket.send(bytes(outputdata[i],'UTF-8'))
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        #https://stackoverflow.com/questions/40320591/python-web-server-socket
        connectionSocket.send(bytes('\nHTTP/1.1 404 Not Found\n\n','UTF-8'))
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()