import sockets 
import struct

class Port:
    
    def __init__(self,port,hostname):
        self.port = port 
        self.hostname = hostname 


    def connect(self):
        global s

        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(self.hostname,self.port)
            print("Connection Successful!")

        except socket.err as error:
            print(f"Connect has failed, ERROR: {error}")


    def send(self,host = None, port_number = None):
        global s

        if host and port_number is None:
            host = self.hostname 
            port_number = self.port

        s.bind(host,port_number) 

    def get(self):
        size = struct.unpack('i',self.s.recv(4))[0]
        return self.s.recv(size).decode('ascii')
