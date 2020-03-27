import threading
import time

variavelPart = 1

threadLock = threading.Lock()

class myThread( threading.Thread ):
    def __init__( self, threadID ):
        threading.Thread.__init__( self )
        self.threadID = threadID

    def run( self ):
        print( 'Starting thread #' + str(self.threadID) )
        
        if( self.threadID == 1 ):
            process1( 1 )
        else:
            process2()

        print( 'Exiting thread #' + str(self.threadID) )

def process1( M ):
    global variavelPart
    x = M
    y = M * ( -1 )

    while( 1 ):
        x = x - variavelPart
        y = y + variavelPart
        
        if( x + y != 0 ):
            print( 'Secção critica violada' )
            print( 'X(' + str(x) + ') + Y(' + str(y) + ') = ' + str(x+y) )
            print( 'variavelPart = ' + str(variavelPart) )
            break

def process2():
    global variavelPart

    while( 1 ):
        variavelPart += 1


if __name__ == '__main__':
    
    # creating new threads
    thread1 = myThread( 1 )
    thread2 = myThread( 2 )

    # start new threads
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print( 'Exiting main thread' )