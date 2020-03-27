import socket

SERVER = "127.0.0.1"
PORT = 2000

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
client.connect( (SERVER, PORT) )

while True:
    # inicializaçao do valor do client
    print( "Escolha um valor entre 0-99" )
    out_data = input()
    
    # verificaçao se client quer dar disconnect
    if out_data == 'bye':
        client.sendall( bytes( out_data, 'UTF-8' ) )
        break
    # verficar se valor escolhido está fora do limite 0-99. caso se verifique pedir novo numero ate que esteja correto
    elif (int(out_data) < 0) or (int(out_data) > 99):
        
        while(int(out_data) < 0) or (int(out_data) > 99):
            print( "Valor Inválido! Escolha um numero entre 0-99" )
            out_data = input()
        
        # enviar numero escolhido ao servidor
        client.sendall( bytes( out_data, 'UTF-8' ) )
    else:
        # enviar numero escolhido ao servidor
        client.sendall( bytes( out_data, 'UTF-8' ) )

    # tratamento da resposta do servidor
    in_data = client.recv( 1024 )
    print( "From Server : ", in_data.decode() )
    
client.close()