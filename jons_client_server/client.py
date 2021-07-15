import socket

HOST = '127.0.0.1'    
PORT = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Client connected.')
while True:
    user_input = str(input())  
    if user_input == "exit":  
        break
    mess = user_input.encode()
    s.sendall(mess)