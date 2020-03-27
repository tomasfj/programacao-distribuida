import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name + "\n")
        self.print_time(self.name, self.counter, 5)
        print("Exiting " + self.name + "\n")

    def print_time(self, threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print("%s: %s" %(threadName, time.ctime(time.time())))
            counter -= 1

# Main
if __name__ == '__main__':
    # Criar duas threads
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    #Iniciar as threads criadas
    thread1.start()
    thread2.start()

    #Esperar que as threads terminem a execução
    thread1.join()
    thread2.join()
    print("Exiting Main Thread")