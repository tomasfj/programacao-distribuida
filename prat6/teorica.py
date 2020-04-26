from mpi4py import MPI
import numpy as np

'''
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print('hello world from process ', rank)

# excutar com: mpiexec -np 4 python teorica.py

'''

'''
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank != 0:
    x = 123
    print('I\'m process %s, my variable is %d' %(rank, x))
else:
    x = 321
    print('I\'m process %s, my variable is %d' %(rank, x))

# executar com: mpiexec -np 6 python teorica.py

'''


'''
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    x = 100
    comm.send(x, dest=1, tag=11)
    print('I\'m process %s' % rank)
elif rank == 1:
    x = comm.recv(source=0, tag=11)
    print('I\'m process %s receive data: %s' % (rank, x))

# executar com: mpiexec -np 2 python teorica.py
'''

'''
comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    print('My rank: %s' % rank)
    for proc in range(1, nprocs):
        msg = comm.recv(source=proc, tag=9)
        print('msg from %s: %s'% (proc, msg))
else:
    msg = 'Hello world from process' + str(rank)
    print('My rank: %s' % rank)
    comm.send(msg, dest=0, tag=9)

# executar com: mpiexec -np 5 python teorica.py
'''

'''
comm = MPI.COMM_WORLD
rank = comm.rank

print("my rank is: ", rank)
if rank == 1:
    data_send ='a'
    destination_process = 5
    source_process = 5
    
    #comm.send(data_send, dest=destination_process)
    #data_received = comm.recv(source=source_process)
    data_received = comm.sendrecv(data_send, dest=destination_process, source=source_process)

    print('sending data: %s' % data_send + ' to process %d' %destination_process)
    print('data received is = %s' %data_received)

if rank == 5:
    data_send = 'b'
    destination_process = 1
    source_process = 1

    #comm.send(data_send, dest=destination_process)
    #data_received = comm.recv(source=source_process)
    data_received = comm.sendrecv(data_send, dest=destination_process, source=source_process)

    print('sending data: %s' % data_send + ' to process %d' % destination_process)
    print('data received is = %s' % data_received)

# executar com: mpiexec -np 10 python teorica.py
'''

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


if rank == 0:
    data = np.arange(100, dtype=np.float)
    comm.Send(data, dest=1, tag=10)
elif rank == 1:
    data = np.empty(100, dtype=np.float)
    comm.Recv(data, source=0, tag=10)
    print('Process %s received %s' % (rank, data))

# executar com: mpiexec -np 2 python teorica.py
# send/recv - objetos gerais python, lento
# Send/Recv - arrays continuos, mais rápido
# notar diferença no Recv - o array tem de já existir
