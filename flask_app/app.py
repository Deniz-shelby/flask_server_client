from flask import Flask, render_template, Response
import socket
import cv2 as cv
import pickle

#import client

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

def client():
   print('fuckoff')
   HEADERSIZE = 10
   PORT = 5551
   #Ip ='127.0.0.2'
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
   s.connect((socket.gethostname(), PORT)) # Connect to the server

   while True:
      # user_input = str(input()) # Receive the data from the server
      # if user_input == "exit":    # Check if the user wants to exit
      #    break
      # elif user_input == "send": # Check if the user wants to send a file
      img = cv.imread("no.jpg", 0)

      msg = pickle.dumps(img)
      msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg # Create a header
      s.send(msg)
      msg = s.recv(1024)
      print(msg.decode())
      prediction = msg.decode()
      break
   s.close()
   

# @app.route('/send_client')
def send_client():
   return Response(client())

if __name__ == "__main__":
    app.run(debug=True)