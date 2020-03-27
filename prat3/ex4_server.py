import socket, threading
import random

class ClientThread( threading.Thread ):
    def __init__(self, clientAddress, clientSocket ):
        threading.Thread.__init__(self)
        self.csocket = clientSocket
        self.clientAddress = clientAddress
        print( "New connection added: ", clientAddress )

    def run( self ):
        print( "Connection from: ", self.clientAddress )
        msg = ""
        # inicializaçao do premio de cada cliente
        prize = 0

        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            
            # verificar se o client se disconectou
            if msg == 'bye':
                break

            # gerar numero aleatorio
            lucky_number = random.randint( 0, 99 )
            # incrementar premio a cada jogada
            prize += 1
            
            # mensagem de verificação
            print( "Client number: " + str(msg) + " Server number: " + str(lucky_number) )
            
            # comparar valor enviado pelo cliente com o valor gerado pelo server
            if( int(lucky_number) != int(msg) ):    
                msg = "Continue a tentar, o prémio já é de: " + str(prize)
            else:
                msg = "Parabéns, ganhou: " + str(prize)
                prize = 0

            # envio de resposta
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