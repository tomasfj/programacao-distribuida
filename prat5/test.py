import numpy as np

arr = np.random.random_integers(0, 9, (10,10))
print(arr)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j])


print("linhas = " + str(len(arr)))
print("cols   = " + str(len(arr[0])))