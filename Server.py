import socket
s = socket.socket()
print('The Port is Ready to connect')

port = 6598
s.bind(('', port))
print('')
print(f'The port open for connections is: {port}')
s.listen(5)
#print('Socket is listening')
while True:
    c, addr = s.accept()

    print("Got Connection from", addr)
    message = 'Hello!!'
    c.send(message.encode())
    c.close()
