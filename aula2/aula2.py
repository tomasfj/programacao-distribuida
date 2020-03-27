# import Thread and sleep
from threading import Thread
from time import sleep

class Exemplo1(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = "Hello Parallel example\n"

    def print_message(self):
        print(self.message)

    def run(self):
        print("Thread Starting\n")
        x = 0
        while(x < 10):
            self.print_message()
            sleep(2)
            x += 1
        print("Thread Ended\n")


print("Process Started")

hello_python = Exemplo1()

hello_python.start()

# suspend main process until thread ends
hello_python.join()

print("Process Ended")