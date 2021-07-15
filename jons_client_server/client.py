import socket

HOST = '127.0.0.1'    
PORT = 5005
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
s.connect((HOST, PORT)) #connect to server
print('Client connected.') #print message to console
while True: #loop forever
    user_input = str(input()) #get user input  
    if user_input == "exit":  #if user input is exit, close connection and exit loop
        break #exit loop
    mess = user_input.encode() #encode user input as bytes
    s.sendall(mess)