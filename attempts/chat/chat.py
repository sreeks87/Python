import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind(('',port))
s.listen(5)
while True:
    c,addr = s.accept()
    print "got connection from ", addr
    c.send("Thank you for connecting")
    c.close()
    
    
