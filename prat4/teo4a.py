import threading
import multiprocessing
import random
import time

SIZE = 10000000

def somaParcial(lista, p, u):
    soma = 0
    for i in range(p, u):
        soma += lista[i]
    
    print(soma)
    return(soma)

if __name__ == "__main__":
    start = time.time()
    lista = [random.randint(1, 10) for i in range(SIZE)]
    print("random values %s" %(time.time()-start))

    # sequencial
    print("starting")
    start = time.time()
    somaParcial(lista, 0, SIZE)
    print("Sequencial time = %s" %(time.time()-start))

    # threads
    start = time.time()
    t1 = threading.Thread(target = somaParcial, args=(lista, 0, int(SIZE/2)))
    t2 = threading.Thread(target = somaParcial, args=(lista, int(SIZE/2), SIZE))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Multithreaded time = %s" %(time.time() - start))

    # processos
    start = time.time()
    t1 = multiprocessing.Process(target = somaParcial, args = (lista, 0, int(SIZE/2)))
    t2 = multiprocessing.Process(target = somaParcial, args = (lista, int(SIZE/2), SIZE))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Multiprocessing time = %s" %(time.time()-start))