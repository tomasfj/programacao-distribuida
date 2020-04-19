import psutil
import numpy as np
import multiprocessing as mp
from multiprocessing import Pipe

# gerar array de 10.000.000 valores entre -5 e 5
array_size = 10000000
arr = np.random.randint(low=-5, high=6, size=array_size)

def count(start, end, pipe):
    soma = arr[ [i for i in range(start, end+1)] ].sum()
    #print(soma)
    pipe.send(soma)
    pipe.close()

if __name__ == "__main__":
    SIZE = int(array_size / psutil.cpu_count())
    soma = 0

    # criar array de pipes
    pipes = [ Pipe() for _ in range(psutil.cpu_count()) ]

    p = [
        mp.Process(target=count, args=(i, i+SIZE, pipes[i][0],))  # pipe[i][0], 0=ouput (enviar para o pipe)
        for i in range(psutil.cpu_count())
    ]

    [p.start() for p in p]

    for i in range(psutil.cpu_count()):
        soma += pipes[i][1].recv()      #pipe[i][1], 1=input (receber do pipe)
    
    [p.join() for p in p]
    
    print(soma)