import multiprocessing
import time
import numpy as np

# cria matrizes e coloca os quadrados num file
def pro1(queue, lock, n_matrizes, d):

    for i in range(n_matrizes):
        # calcular matriz de valores aleatorios
        m = np.random.rand(d, d)
        
        # coloca a matriz numa queue
        queue.put(m)
        
        # lock até que o quadrado da matriz seja calculado por pro2()
        lock.acquire()

        # escrever quadrado da matriz num file
        with open("ex3.txt", "ab") as f:
            np.savetxt(f, queue.get(), footer="\n")

    # indicar à pro2() que terminou a inserção de valores na queue
    queue.put("done")

# calcula quadrados das matrizes
def pro2(queue, lock):
    while True:
        # retira matriz da queue
        m = queue.get()
        
        # verificar se a inserção na queue já terminou. Devolve warning por incompatibilidade na comparação de objeto numpy e string
        if(m == "done"):
            break

        # calculo do quadrado da matriz. Colocar resultado na queue
        queue.put(m*2)
        
        # libertar lock para que pro1() possa continuar
        lock.release()
    
if __name__ == "__main__":
    queue = multiprocessing.Queue()
    lock = multiprocessing.Lock()

    # numero de matrizes a ser criadas
    n_matrizes = 2
    # dimensão das matrizes
    d = 2

    start = time.time()
    t1 = multiprocessing.Process(target=pro1, args=(queue, lock, n_matrizes, d))
    t2 = multiprocessing.Process(target=pro2, args=(queue, lock))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Execution time = %s" %(time.time()-start))
