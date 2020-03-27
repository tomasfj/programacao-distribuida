import time
import threading
from threading import Thread, Event
import random

items = []
event = Event()

class consumer(Thread):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print( 'Cons. notify : %d popped from list by %s' %(item, self.name) )
            self.event.clear()
            print( 'Produce notify : event cleared by %s \n' % self.name )

class producer( Thread ):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run( self ):
        for i in range( 100 ):
            time.sleep( 2 )
            item = random.randint( 0, 256 )
            self.items.append( item )
            print( 'Prod. notify : item %d appended to list by %s' %(item, self.name) )
            print( 'Producer notify : event set by %s' % self.name )
            self.event.set()

if __name__ == '__main__':
    t1 = producer(items, event)
    t2 = consumer(items, event)
    t1.start()
    t2.start()
    t1.join()
    t2.join()