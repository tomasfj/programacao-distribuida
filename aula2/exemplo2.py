import threading

def function(i):
    print("function called by thread %i \n" %i)
    return

#threads = []

#for i in range(5):
#    t = threading.Thread(target = function, args=(i,))
#    threads.append(t)
#    t.start()
#    t.join()

# desta forma todas as threads são chamadas em simultâneo
threads = [threading.Thread(target = function, args=(i,)) for i in range(5)]
[t.start() for t in threads]
[t.join() for t in threads]