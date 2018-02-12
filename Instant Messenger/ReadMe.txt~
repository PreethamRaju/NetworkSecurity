---------------------IM with RSA Encryption --------------------------

Here, Instant Messenger is created with a UDP socket.
Each character is encrypted by RSA encryption.
RSA - Rivest Shamir Adleman encryption is an asymmetric key encryption and relies on 2 keys private and public key for encryption and decryption rspectively and can be inversely used. The private key is kept secret but the public key can be published.

Design

1. Two prime numbers p and q are chosen.
2. n=p*q
3. phi = (p-1)(q-1)
4. e is chosen such that it is coprime to phi.
5. inverse of e is computed. i.e (e*d) mod(phi) =1
6. e is the private key.
7. d is the public key used for decrytpion.


Files Submitted

1. Alice.py
2. Bob.py

These programs represent two ends of Instant Messaging.

Execution

1. Open the terminal (2- To represent two ends of IM) and go to the terminal where the program is saved.
2. Run the Client program first (Alice) by the command "python Alice.py".
3. In the other terminal, run the server end (Bob) with the command "python Bob.py"
4. Now start the chat from Bob's side where it says "Me:" and press enter to send the message.
5. Notice in the other terminal the message being received by alice.
6. Now type what you intend to say in the Alice's side.

Design document

1. import socket - This module gives access to BSD socket interface.
The functions under this module are

socket.gethostbyname('localhost') returns the IP address of the host

socket.socket(family,type,protocol) creates a socket of the given address family, socket type and protocol number.

socket.bind(address) binds the socket to the address

sock.sendto(),sock.recvfrom() are used to send and receive data for a UDP socket 

2. import time - This is used for the function time.sleep() to syncronize the server and the client


3. import math - This module gives access to the math.pow(x,y) instruction to compute x raised to y.
