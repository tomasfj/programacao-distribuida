from threading import Thread, Condition
import time

items = []
condition = Condition()

class consumer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global condition
        global items
        condition.acquire()

        if len(items) == 0:
            print( "consumer notify : no item to consume" )
            condition.wait()

        items.pop()
        print( "consumer notify : consumed 1 item" )
        print( "consumer notify : items to consume are " + str(len(items)) )

        condition.notify()
        condition.release()

    def run(self):
        for i in range(0,20):
            time.sleep(10)
            self.consume()

class producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print( "producer notify : items produced are " + str(len(items)) )
            print( "producer notify: stop the production!" )

        items.append(1)
        print( "producer notify : total items produced " + str(len(items)) )
        condition.notify()
        condition.release()
    
    def run(self):
        for i in range(0,20):
            time.sleep(5)
            self.produce()


if __name__ == "__main__":
    producer = producer()
    consumer = consumer()

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
