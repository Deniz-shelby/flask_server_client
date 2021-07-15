import socket
import cv2 as cv
import pickle

HEADERSIZE = 10
PORT = 5551

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), PORT))

while True:
    user_input = str(input())
    if user_input == "exit":
        break
    elif user_input == "send":
        img = cv.imread("no.jpg", 0)

        msg = pickle.dumps(img)
        msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg
        s.send(msg)
        msg = s.recv(1024)
        print(msg.decode())
        user_input = ''
