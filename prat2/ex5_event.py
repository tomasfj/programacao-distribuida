from threading import Thread, Event
import time

variavelPart = 1
event = Event()

class myThread( Thread ):
    def __init__( self, threadID, event ):
        Thread.__init__(self)
        self.threadID = threadID
        self.event = event

    def run( self ):
        print( 'Starting thread #' + str(self.threadID) )
        
        if( self.threadID == 1 ):
            process1( 1, self.event )
        else:
            process2( self.event )

        print( 'Exiting thread #' + str(self.threadID) )

def process1( M, event ):
    global variavelPart
    x = M
    y = M * ( -1 )

    event.wait()
    
    while( 1 ):
        x = x - variavelPart
        y = y + variavelPart
        
        if( x + y != 0 ):
            print( 'Secção critica violada' )
            print( 'X(' + str(x) + ') + Y(' + str(y) + ') = ' + str(x+y) )
            print( 'variavelPart = ' + str(variavelPart) )
            break
    
    event.clear()

def process2(event):
    global variavelPart

    while( 1 ):
        variavelPart += 1
    
    event.set()


if __name__ == '__main__':
    
    # creating new threads
    thread1 = myThread( 1, event )
    thread2 = myThread( 2, event )

    # start new threads
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print( 'Exiting main thread' )