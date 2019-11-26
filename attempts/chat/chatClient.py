import socket
s = socket.socket()
host = socket.gethostname()
port  =  12345
s.connect((host,port))
while True:
    print (s.recv(1024))
    s.send("hello")
s.close()
