# Implementar um programa em que todos os processos
# diferentes do processo 0, enviam uma mensagem para o processo 0 
# com a mensagem “Olá sou o processo nº X”.a) 
# O que acontece se executa com apenas um processo?

from mpi4py import MPI

comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    print('Exexcutando o proccesso: %s' % rank)
    for proc in range(1, nprocs):
        msg = comm.recv(source=proc, tag=3)
        print('msg from %s: %s'% (proc, msg))
else:
    print('Executando o processo: %s' % rank)
    msg = 'olá sou o processo nº' + str(rank)
    comm.send(msg, dest=0, tag=3)

# excutar com: mpiexec -np 5 python ex3.py

# a) O que acontece se executa com apenas um processo?
# Resp.: Apenas o primeiro processo corre, e como não recebe nenhuma mensagem nada é apresentado