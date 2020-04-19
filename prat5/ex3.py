import psutil
import numpy as np
import multiprocessing as mp
from multiprocessing import Pipe
import math


def readFile(n, pipe):
    with open("f"+str(n)+".txt") as f:
        soma = sum([ fx(int(i)) for i in next(f).split() ])
    
    pipe.send(soma)
    pipe.close()

def fx(x):
    if(x%2 == 0):
        r = math.sin(x)
    else:
        r = math.cos(x)
    
    return r

if __name__ == "__main__":
    num_processos = 2 * psutil.cpu_count()
    soma = 0
    pipes = [ Pipe() for _ in range(num_processos) ]

    p = [
        mp.Process(target=readFile, args=(i, pipes[i-1][0],))
        for i in range(1, num_processos+1)
    ]

    [p.start() for p in p]

    for i in range(num_processos):
        soma += pipes[i][1].recv()

    [p.join() for p in p]

    print(soma)
    print("DONE")