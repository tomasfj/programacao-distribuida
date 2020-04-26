# Ficha Prática 6 - exercício 4
# Escreva um programa onde um processo com rank K envie uma mensagem ao processo com rank (K+1)%p. 
# A mensagem é a string “Olá, do processo K”, e não deve utilizar wildcards.
# Execute oprograma com vários processos.
# ----
# Realizado por:
# Tomás Jerónimo, M9988

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# mensagem para enviar ao processo (K+1)%p
msg = 'Olá, do processo %s' % rank

# envio da mensagem para o processo (K+1)%p
comm.send(msg, dest=(rank+1)%size )
# receber mensagem do processo K-1
data_received = comm.recv(source=rank-1)

# apresentação da mensagem recebida
print('Rank: %s  -  msg: %s' % (rank, data_received) )


# excutar: mpiexec -np 5 python3 ex4.py