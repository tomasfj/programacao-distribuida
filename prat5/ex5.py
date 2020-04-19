import psutil
import numpy as np
import multiprocessing as mp
from multiprocessing import Pipe, Barrier, Pool
import math


def fx(x):
    if(x%2 == 0):
        r = math.sin(x)
    else:
        r = math.cos(x)
    
    return r

if __name__ == "__main__":

    arr = np.arange(2 * psutil.cpu_count() * 1000 - 1)

    pool = Pool(processes=psutil.cpu_count())

    pool_outputs = pool.map(fx, arr)

    print("Somatorio = %f" % sum(pool_outputs))

    print("DONE")