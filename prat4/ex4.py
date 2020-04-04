import time
import numpy as np
import queue


def gerarMatrizes(n_matrizes, d):
    
    for i in range(n_matrizes):
        m = (np.random.rand(d,d))*2

        with open("ex4.txt", "ab") as f:
            np.savetxt(f, m, footer="\n")


if __name__ == "__main__":
    n_matrizes = 100
    d = 100

    start = time.time()

    gerarMatrizes(n_matrizes, d)

    print("Execution time = %.4f seconds" %(time.time()-start))



'''
Resultados Execução Sequencial (ex4):
n_matrizes  | dimensão   | tempo de execução
---------------------------------------------
2           | 2x2       | 0.0123 segundos
2           | 10x10     | 0.0138 segundos
10          | 2x2       | 0.0655 segundos
10          | 10x10     | 0.0664 segundos
100         | 100x100   | 1.4110 segundos
200         | 200x200   | 7.4510 segundos

Resultados Execução por Processos (ex3):
n_matrizes  | dimensão   | tempo de execução
---------------------------------------------
2           | 2x2       | 0.0291 segundos
2           | 10x10     | 0.0316 segundos
10          | 2x2       | 0.0815 segundos
10          | 10x10     | 0.0850 segundos
100         | 100x100   | 1.5178 segundos
200         | 200x200   | 8.0224 segundos

Análise: Verifica-se uma ligeira vantagem na solução sequencial, 
no entanto isto pode ser explicado pelo facto de não serem 
utilizados mais processos para dividir o trabalho do proc1() 
(primeiro processo onde as matrizes são geradas e guardadas).
Para além disto, a solução por processos tem a "desvantagem" (em
termos temporais) de utilizar um lock() e uma queue para garantir 
a comunicação entre os dois processos. 
'''