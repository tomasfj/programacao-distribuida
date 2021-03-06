import socket, threading

class ClientThread( threading.Thread ):
    def __init__(self, clientAddress, clientSocket ):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        self.clientAddress = clientAddress
        print( "New connection added: ", clientAddress )

    def run( self ):
        print( "Connection from: ", self.clientAddress )
        msg = ""
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            
            if msg == 'bye':
                break
            
            print( 'from client : ' + str(msg) )
            self.csocket.send( bytes( msg, 'UTF-8' ) )
        
        print( "Client at ", str(self.clientAddress) + " disconnected..." )

LOCALHOST = "127.0.0.1"
PORT = 2000

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
server.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
server.bind( (LOCALHOST, PORT) )

print( "Server started" )
print( "Waiting for client request.." )

while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread( clientAddress, clientsock )
    newthread.start()