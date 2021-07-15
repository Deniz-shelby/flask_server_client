import socket

HOST = '127.0.0.1'    
PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP SOCKET
s.bind((HOST, PORT)) # Bind the socket to the host and port
s.listen(1) # 1 is the number of clients that can queue
clientsocket, addr = s.accept() # Accept the connection
print('Client connected: ', addr) # Print the address of the client

while True: # Loop to receive data
    data = clientsocket.recv(1024) # 1024 is the buffer size
    if not data or data == "": # If data is null or empty
        break # Exit the loop
    decoded_data = data.decode() # Decode the data
    clientsocket.send(decoded_data) # Print the data