from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank != 0:
    x = 123
    print("I'm process %s, my variable is %d" %(rank,x))

else:
    x = 321
    print("I'm process %s, my variable is %d" %(rank,x))