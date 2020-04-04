'''
Estudar os tempos de execução:
. sequencial
. multithread
. multiprocessos 
para cada uma das funções: 
. fibonacci
. url
. readFile

Analisar resultados.
'''

from threading import Thread
import urllib.request
import time
from multiprocessing import Process

# Execução Sequencial
class nothreads_object(object):
    def run(self):
        #function_to_run_fibbo()
        function_to_run_url()
        #function_to_run_file()

def non_threaded(num_iter):
    funcs = []
    
    for i in range( int(num_iter) ):
        funcs.append(nothreads_object())
    
    for i in funcs:
        i.run()

# Execução multithreaded
class threads_object(Thread):
    def run(self):
        #function_to_run_fibbo()
        function_to_run_url()
        #function_to_run_file()

def threaded(num_threads):
    funcs = []
    
    for i in range( int(num_threads) ):
        funcs.append( threads_object() )
    
    for i in funcs:
        i.start()
    
    for i in funcs:
        i.join()

def show_results(func_name, results):
    print("%-23s %4.6f seconds" %(func_name, results))


# Execução multiprocessing
class process_object(Process):
    def run(self):
        #function_to_run_fibbo()
        function_to_run_url()
        #function_to_run_file()

def processed(num_processes):
    funcs = []

    for i in range(int(num_processes)):
        funcs.append(process_object())

    for i in funcs:
        i.start()

    for i in funcs:
        i.join()



# functions to run
def function_to_run_fibbo():
    #Fibonacci
    a = 0
    b = 1
    for i in range(100000):
        a = b
        b = a+b

def function_to_run_url():
    for i in range(10):
        with urllib.request.urlopen("https://google.com") as f:
            f.read(1024)

def function_to_run_file():
    file = open("test.dat", "rb")
    size = 1024
    for i in range(1000):
        file.read(size)


# main
if __name__ == "__main__":
    num_threads = [1,2,4,8]
    print("Starting tests")

    for i in num_threads:

        # sequencial
        start = time.time()
        non_threaded(i)
        executionTime = time.time() - start
        show_results("non_threaded (%s iters)" %i, executionTime)

        # threaded
        start = time.time()
        threaded(i)
        executionTime = time.time() - start
        show_results("threaded (%s threads)" % i, executionTime)

        # processed
        start = time.time()
        processed(i)
        executionTime = time.time() - start
        show_results("processed (%s processes)" %i, executionTime)

    print("Iterations complete")


'''
Apresentação de resultados:

Fibonacci (F1)
Threads | Sequencial    | Threaded      | Processed
1       | 0.140220 s    | 0.142309 s    | 0.171712 s
2       | 0.278199 s    | 0.276906 s    | 0.162182 s
4       | 0.592690 s    | 0.568686 s    | 0.209662 s
8       | 1.138981 s    | 1.127482 s    | 0.313482 s

Análise: Durante todo o processo a execução Sequencial e Threaded obtiveram
resultados semelhantes enquanto que a execução por Processos obteve sempre 
melhores resultados, excepto na primeira execução (1 thread).
À medida que o número de threads aumentou a execução por Processos 
destacou-se em relação às outras (no que toca ao tempo de execução).

URL (F2)
Threads | Sequencial    | Threaded      | Processed
1       | 4.237558 s    | 4.487031 s    | 4.510582 s
2       | 8.526937 s    | 5.060087 s    | 4.090834 s
4       | 17.99895 s    | 5.126970 s    | 4.814211 s
8       | 33.76315 s    | 5.157609 s    | 5.259390 s

Análise: À medida que o número de threads/processos aumentou a solução
sequencial verificou um aumento no tempo de execução enquanto que as outras
duas soluções se mantiveram relativamente constantes.

ReadFile (F3)
Threads | Sequencial    | Threaded      | Processed
1       | 0.005640 s    | 0.005557 s    | 0.014764 s
2       | 0.010888 s    | 0.009978 s    | 0.019795 s
4       | 0.021694 s    | 0.054544 s    | 0.026143 s
8       | 0.043437 s    | 0.111490 s    | 0.044909 s

Análise: Neste caso a solução sequencial foi a apresentou melhores
resultados e a solução threaded acabou por ser a mais demorada.
'''