import threading
import time

variavelPart = 1

# defining semaphore with the initial counter
semaphore = threading.Semaphore(1)

def process1( M ):

    global variavelPart
    x = M
    y = M * ( -1 )
    
    # decrease semaphore counter
    semaphore.acquire()
    
    x = x - variavelPart
    y = y + variavelPart
    print( 'X(' + str(x) + ') + Y(' + str(y) + ') = ' + str(x+y) )
    print( 'variavelPart = ' + str(variavelPart) )
    
    if( x + y != 0 ):
        print( 'Secção critica violada' )

def process2():
    global variavelPart

    variavelPart += 1
    print( 'Increased variavelPart to ' + str(variavelPart) )

    # increase semaphore counter
    semaphore.release()
    time.sleep(2)
    


if __name__ == '__main__':
    while(1):
        t1 = threading.Thread( target = process1(1) )
        t2 = threading.Thread( target = process2() )
        t1.start()
        t2.start()
        #t1.join()
        #t2.join()

    print( 'Exiting main thread' )