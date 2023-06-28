import socket
s = socket.socket()

port = 6598

s.connect(('192.168.0.105', port))

print(s.recv(1024))
s.close()