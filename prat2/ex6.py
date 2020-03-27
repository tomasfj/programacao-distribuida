from threading import Thread, Event
import time

XPTO = 0
event = Event()

# metodos 'ler' e 'escrever'
def ler( xpto, event ):

    # waiting for event to become TRUE
    event.wait()
    print( 'XPTO = ' + str(xpto) )
    time.sleep(2)
    
def escrever( xpto, event ):

    # set event to FALSE
    event.clear()

    xpto += 100
    xpto -= 100

    # set event to TRUE
    event.set()


class rw( Thread ):
    def __init__( self, xpto, event, flag ):
        Thread.__init__( self )
        self.xpto = xpto
        self.event = event
        self.flag = flag

    def run( self ):

        if( self.flag == 'r' ):
            ler( self.xpto, self.event )
        if( self.flag == 'w'):
            escrever( self.xpto, self.event )


class leitor( Thread ):
    def __init__( self, xpto, event ):
        Thread.__init__( self )
        self.xpto = xpto
        self.event = event
    
    def run( self ):
        while( 1 ):
            ler( self.xpto, self.event )


class escritor( Thread ):
    def __init__(self, xpto, event):
        Thread.__init__( self )
        self.xpto = xpto
        self.event = event
    
    def run( self ):   
        while( 1 ):
            escrever( self.xpto,self.event )



if __name__ == '__main__':

    rw_r = rw( XPTO, event, 'r' )
    rw_w = rw( XPTO, event, 'w' )

    leitor1 = leitor( XPTO, event )
    leitor2 = leitor( XPTO, event )
    leitor3 = leitor( XPTO, event )
    
    escritor1 = escritor( XPTO, event )
    escritor2 = escritor( XPTO, event )

    leitor1.start()
    leitor2.start()
    leitor3.start()
    
    escritor1.start()
    escritor2.start()

    rw_r.start()
    rw_w.start()