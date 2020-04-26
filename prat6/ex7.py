# Ficha Prática 6 - exercício 7
# Construa um programa para calcular a média de um array de valores, 
# usando as operações MPI Scatter e MPI Gather em mpi4py
# -----
# Realizado por:
# Tomás Jerónimo, M9988


import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# tamanho dos arrays do scatter
buff_size = 5
# iniciialização do vetor onde cada processo receberá os valores do scatter
rec_toScatter = np.empty(buff_size, dtype=np.float)
# vetor inicial de valores para serem dividos pelo scatter. apenas é definido no processo 0
senddata_toScatter = None

# processo 0
if rank == 0:
    # vetor inicial de valores para serem dividos pelo scatter
    senddata_toScatter = np.arange(size*buff_size, dtype=np.float)
    # verificação do vetor gerado
    print('Data to Scatter: ')
    print(senddata_toScatter)

# scatter do vetor gerado pelo processo 0
comm.Scatter(senddata_toScatter, rec_toScatter, root=0)
# verificação
print('Rank %s' % rank + ' shared: %s' % rec_toScatter)

# inicialização do vetor para receber os valores do gather
rec_toGather = np.zeros(size, dtype=np.float)

# envio do somatório de cada vetor do scatter para o gather
senddata_toGather = np.sum(rec_toScatter)
comm.Gather(senddata_toGather, rec_toGather, root=0)

# recolha dos dados do gather no processo 0
if rank == 0:
    # calculo da média. soma das somas parciais dos vetores do scatter e divisão pelo tamanho da matriz inicial
    media = (np.sum(rec_toGather) / (size*buff_size) )
    print('Média = ' + str( media ) )