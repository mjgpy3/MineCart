#!/usr/bin/python

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 915                  # Reserve a port for your service.

s.connect((host, port))

s.send('{ "artist" : "MIA", "song" : "Paper Planes"}')

print s.recv(10000)
s.close                     # Close the socket when done
