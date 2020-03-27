import threading
import time

a = []
for i in range(1000):
    a.append(i+1)

soma = 0


class myThread(threading.Thread):
    def __init__(self, name, flag):
        threading.Thread.__init__(self)
        self.name = name
        self.flag = flag
        self.resultado = 0

    def run(self):
        print("Starting " + self.name + "\n")

    
    def soma(self, flag):
        global a
        sum1 = 0
        print("soma")
        for i in range(self.flag, 1000, 2):
            sum1 = sum1 + a[i]

        self.setResultado(sum1)
        global soma
        soma = soma + sum1

    def getResultado(self):
        return self.resultado

    def setResultado(self, x):
        self.resultado = x

    def setGlobalSoma(self, x):
        global soma
        soma = x


if __name__ == '__main__':
    thread1 = myThread("Thread-1", 0)
    thread2 = myThread("Thread-2", 1)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print( soma )
    print( soma )

    print( "END" )