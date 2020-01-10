import socket
import struct

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost', 1234)
client.connect(server_address)

for i in range(100):
    size = struct.unpack('i',client.recv(4))[0]
    str_data = client.recv(size)
    print('Data size : %s Data Value: %s' %(size,str_data.decode('ascii')))


client.sendall(b'stop') # sending anything back closes the connection
