# Ficha Prática 6 - exercício 5
# No programa que se segue, para comunicar entre processos, usar apenas as instruções send e recv.
# O processo 0 deve criar uma mensagem com uma string que contenha o seu nome. 
# Esta mensagem deve ser passada entre os processadores arranjados logicamente num anel P0,P1,..Pn-1 
# até a mensagem chegar novamente ao processo com rank zero onde a mensagem será impressano ecrã.
# ----
# Realizado por:
# Tomás Jerónimo, M9988

from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# processo 0
if rank == 0:
    # mensagem a enviar
    msg = 'Rank %s' % rank

    # envio da mensagem para o próximo processo
    comm.send(msg, dest=rank+1)
    
    # receber mensagem do último processo
    rec = comm.recv(source=size-1)
    # append do do nome do processo 0 à mensagem
    msg = rec + ' - Rank %s' % rank
    # apresentação da mensagem final
    print(msg)

# processos excepto último 
elif rank < size-1:
    # receber mensagem do processo anterior
    rec = comm.recv(source=rank-1)
    # append do nome do processo à mensagem
    msg = rec + ' - Rank %s' % rank
    # envio da mensagem ao próximo processo
    comm.send(msg, dest=rank+1)
# último processo
else:
    # receber mensagem do processo anterior
    rec = comm.recv(source=rank-1)
    # append do nome do processo à mensagem
    msg = rec + ' - Rank %s' % rank
    # envio da mensagem ao próximo processo
    comm.send(msg, dest=0)


# executar: mpiexec -np 5 python3 ex5.py