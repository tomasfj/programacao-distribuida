import threading
import time
import random

semaphore = threading.Semaphore(0)

def consumer():
    global item
    print( "consumer is waiting" )
    semaphore.acquire()
    print( "Consumer notify: consumed item number %s " %item )

def producer():
    global item
    time.sleep(2)
    item = random.randint(0,1000)
    print("producer notify : produced item numer %s " %item )
    semaphore.release()

if __name__ == "__main__":
    for i in range(0,5):
        t1 = threading.Thread( target=producer )
        t2 = threading.Thread( target=consumer )
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    print( "program terminated" )