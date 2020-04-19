'''
Resolução do exercício 6 da Ficha Prática 5, Aula 17 de abril
Tomás Jerónimo, M9988, Mestrado Engenharia Informática

Notas:
    - número de cores do pc: 8
'''

import psutil
import numpy as np
import multiprocessing as mp
from multiprocessing import Pool
import math


def fx(x):
    if(x%2 == 0):
        r = math.sin(x)
    else:
        r = math.cos(x)
    
    return r

if __name__ == "__main__":

    # criar array com valores entre 0 e (2 * psutil.cpu_count() * 1000 - 1)
    arr = np.arange(2 * psutil.cpu_count() * 1000 - 1)

    # inicialização da Pool()
    pool = Pool(processes=psutil.cpu_count())

    # aplicar a cada elemento de arr a função fx de forma assincrona
    pool_outputs = pool.map_async(fx, arr)

    # pedir nome do ficheiro ao user, equanto espera pelo fim da Pool
    filename = input("Nome do ficheiro: ")

    # esperar que Pool termine
    pool_outputs.wait()

    # guardar resultados da Pool no ficheiro, com o nome escolhido pelo user
    with open(filename, "w") as file:
        for i in pool_outputs.get():
            file.write(str(i) + " ")

    print("DONE")