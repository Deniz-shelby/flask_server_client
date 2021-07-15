from socket import socket, AF_INET, SOCK_STREAM
import pickle
import torch
import numpy as np
import torch.nn.functional as F

model = torch.load("Best_model2.pth")

HEADERSIZE = 10

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 5551))
s.listen(5)

# while True:
full_msg = b''
new_msg = True
connection, address = s.accept()
print("Connected from", address)

while True:
    msg = connection.recv(16)
    if new_msg:
        # print(f'new message legnth:{msg[:HEADERSIZE]}')
        msg_len = int(msg[:HEADERSIZE])
        new_msg = False
    full_msg += msg

    if len(full_msg) - HEADERSIZE == msg_len:
        # print('Full msg recvd')

        img = pickle.loads(full_msg[HEADERSIZE:])

        new_msg = True
        full_msg = b''
        if new_msg:
            print("yes")
            print(type(img))
            img = np.array(img, dtype="float32")
            tensor_img = torch.from_numpy(img).reshape(784, 1)
            tensor_img = F.normalize(tensor_img)
            tensor_img = tensor_img.view((-1, 784))
            print(torch.argmax(model(tensor_img)))
            pred = str(torch.argmax(model(tensor_img)).item()).encode()
            connection.send(pred)

