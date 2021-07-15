import socket

HOST = '127.0.0.1'    
PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP SOCKET
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()  
print('Client connected: ', addr)


while True:
    data = conn.recv(1024)
    if not data or data == "":
        break
    decoded_data = data.decode()
    print(decoded_data)