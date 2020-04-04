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
from urllib.request import urlopen
import time
from multiprocessing import Process

# Execução Sequencial
class nothreads_object(object):
    def run(self):
        #function_to_run_fibbo()
        #function_to_run_url()
        function_to_run_file()

def non_threaded(num_iter):
    funcs = []
    
    for i in range( int(num_iter) ):
        funcs.append(nothreads_object())
    
    for i in funcs:
        i.run()

# Execução multithreaded
class threads_object(Thread):
    def __init__(self, size, begin, num_threads):
        Thread.__init__(self)
        self.size = size
        self.begin = begin
        self.num_threads = num_threads

    def run(self):
        #function_to_run_fibbo()
        #function_to_run_url2(self.num_threads)
        function_to_run_file2(self.size, self.begin)

def threaded(num_threads, size):
    funcs = []
    begin = 0
    
    for i in range( int(num_threads) ):
        funcs.append( threads_object(size, begin, num_threads) )
        begin += size

    for i in funcs:
        i.start()
    
    for i in funcs:
        i.join()

def show_results(func_name, results):
    print("%-23s %4.6f seconds" %(func_name, results))


# Execução multiprocessing
class process_object(Process):
    def __init__( self, size, begin, num_processes) :
        Process.__init__( self )
        self.size = size
        self.begin = begin
        self.num_processes = num_processes


    def run(self):
        #function_to_run_fibbo()
        #function_to_run_url2(self.num_processes)
        function_to_run_file2(self.size, self.begin)

def processed(num_processes, size):
    funcs = []
    begin = 0

    for i in range(int(num_processes)):
        funcs.append(process_object(size, begin, num_processes))
        begin += size

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
        with urlopen("https://google.com") as f:
            f.read(1024)

def function_to_run_url2(n):
    for i in range(int(10/n)):
        with urlopen("https://google.com") as f:
            f.read(1024)

def function_to_run_file():
    file = open("test.dat", "rb")
    size = 1024
    for i in range(1000):
        file.read(size)

def function_to_run_file2(size, begin):
    file = open("test.dat", "rb")
    #print("New Process \n" + str(file.read(size)) + "\n" )
    file.seek(begin, 0)
    file.read(size)




# main
if __name__ == "__main__":
    num_threads = [1,2,4,8]
    print("Starting tests")

    for i in num_threads:

        file_size = 30477
        bytes_per_thread = int(file_size/i)
        #print("bytes to read = " + str(bytes_per_thread))

        # sequencial
        start = time.time()
        non_threaded(i)
        executionTime = time.time() - start
        show_results("non_threaded (%s iters)" %i, executionTime)

        # threaded
        start = time.time()
        threaded(i, bytes_per_thread)
        executionTime = time.time() - start
        show_results("threaded (%s threads)" % i, executionTime)

        # processed
        start = time.time()
        processed(i, bytes_per_thread)
        executionTime = time.time() - start
        show_results("processed (%s processes)" %i, executionTime)

    print("Iterations complete")

'''
Apresentação de resultados:

URL (F2)
Threads | Sequencial    | Threaded      | Processed
1       | 4.822540 s    | 4.680710 s    | 4.408484 s
2       | 8.000374 s    | 2.740546 s    | 2.345379 s
4       | 17.84863 s    | 0.820597 s    | 1.173235 s
8       | 36.20456 s    | 0.431148 s    | 0.483990 s

Análise: Comparando estes resultados com os obtidos na alínea anterior,
é possível observar uma clara redução nos tempos de execução das soluções
por Threads e por Processos. Esta redução é mais evidente quanto mais forem
o número de threads/processos utilizados. Isto é explicado pelo facto de o
trabalho ter sido dividido pelas várias threads/processos, ou seja quanto 
mais threads/processos estiverem disponíveis menor será o trabalho realizado por
cada um (verifica-se que a cada aumento de thread/processo o tempo de 
execução cai para metade).

ReadFile (F3)
Threads | Sequencial    | Threaded      | Processed
1       | 0.019312 s    | 0.001796 s    | 0.013275 s
2       | 0.017056 s    | 0.005804 s    | 0.022022 s
4       | 0.034661 s    | 0.005016 s    | 0.032872 s
8       | 0.058670 s    | 0.008125 s    | 0.058772 s

Análise: Neste exemplo os resultados obtidos parecem ser contraditórios aos
resultados e observações feitas anteriormente, pois o tempo de execução nas
soluções com threads e processos aumenta consoante o aumento no número de
threads/processos. Isto pode no entanto resultar da abertura e fecho de 
ficheiros e da utilização da função seek() para que cada thread/processo
não realize a mesma leitura que as threads/processos anteriores. Com o 
aumento do número de threads/processos aumenta também o número de utilizações
destas funções e daí o aumento no tempo de execução. Parece então que para a
leitura de ficheiros estas soluções seriam menos preferíveis, no entanto, 
se para além da leitura do ficheiro fosse necessário realizar operações que
consumissem mais tempo/recursos, então estas soluções, provavelmente, já
iriam fornecer uma vantagem temporal.
'''