import psutil
import numpy as np
import multiprocessing as mp


def makeFile(start, end, n):
    with open("f"+str(n)+".txt", "w") as file:
        for i in range(start, end):
            file.write(str(i) + " ")


if __name__ == "__main__":
    num_processos = 2 * psutil.cpu_count()

    p = [
        mp.Process(target=makeFile, args=((i-1)*1000, (i*1000)-1, i,))
        for i in range(1, num_processos+1)
    ]

    [p.start() for p in p]
    [p.join() for p in p]

    print("DONE")