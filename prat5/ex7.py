'''
Resolução do exercício 7 da Ficha Prática 5, Aula 17 de abril
Tomás Jerónimo, M9988, Mestrado Engenharia Informática

Notas:
    - Número de cores do pc: 8
'''

import numpy as np
import multiprocessing as mp
from multiprocessing import Pipe

# função que faz a soma dos valores de cada vizinho
def soma(x1, x2, x3, x4, x5, x6, x7, x8):
    return(x1+x2+x3+x4+x5+x6+x7+x8)

# função que faz a validação da posição de cada vizinho
def isValid(x, y, l, c):
    if( (x < 0) or (x >= l) ):
        return(False)
    elif( (y < 0) or (y >= c) ):
        return(False)
    else:
        return(True)

# função que recebe uma parte da matriz e cria uma nova matriz onde cada valor é a soma dos vizinhos da matriz original
def alterMatrix(m, pipe):

    # criar uma matriz de zeros com as mesmas dimensões que a matriz recebida
    m2 = np.zeros((len(m), len(m[0])))

    '''
    Para cada célula (x) somar os seus vizinhos (x1, x2, x3, x4, x5, x6, x7, x8), caso a sua posição seja válida.
    Para a posição dos vizinhos ser válida:
        . o valor de i não deve ser menor que 0 nem maior que o número de linhas (len(m))
        . o valor de j não deve ser menor que 0 nem maior que o número de colunas (len(m[i]))  
    
    A seguir apresenta-se uma representação de uma célula, com coordenadas (i, j), e de cada um dos seus vizinhos:
    
    x1(i-1, j-1)  x2(i-1, j)  x3(i-1, j+1)
    x4(i, j-1)    x(i, j)     x5(i, j+1)
    x6(i+1, j-1)  x7(i+1, j)  x8(i+1, j+1) 
    
    '''

    # iteração da matriz recebida para somar os vizinhos de cada célula
    for i in range(len(m)):
        for j in range(len(m[i])):
            # validar se vizinho x1 é valido. caso seja adicionar o seu valor a x1. caso nao seja x1=0
            if( isValid(i-1, j-1, len(m), len(m[i])) ):
                x1 = m[i-1][j-1]
            else:
                x1 = 0
            # validar se vizinho x2 é valido. caso seja adicionar o seu valor a x2. caso nao seja x2=0
            if( isValid(i-1, j, len(m), len(m[i])) ):
                x2 = m[i-1][j]
            else:
                x2 = 0
            # validar se vizinho x3 é valido. caso seja adicionar o seu valor a x3. caso nao seja x3=0
            if( isValid(i-1, j+1, len(m), len(m[i])) ):
                x3 = m[i-1][j+1]
            else:
                x3 = 0
            # validar se vizinho x4 é valido. caso seja adicionar o seu valor a x4. caso nao seja x4=0
            if( isValid(i, j-1, len(m), len(m[i])) ):
                x4 = m[i][j-1]
            else:
                x4 = 0
            # validar se vizinho x5 é valido. caso seja adicionar o seu valor a x5. caso nao seja x5=0
            if( isValid(i, j+1, len(m), len(m[i])) ):
                x5 = m[i][j+1]
            else:
                x5 = 0
            # validar se vizinho x6 é valido. caso seja adicionar o seu valor a x6. caso nao seja x6=0
            if( isValid(i+1, j-1, len(m), len(m[i])) ):
                x6 = m[i+1][j-1]
            else:
                x6 = 0
            # validar se vizinho x7 é valido. caso seja adicionar o seu valor a x7. caso nao seja x7=0
            if( isValid(i+1, j, len(m), len(m[i])) ):
                x7 = m[i+1][j]
            else:
                x7 = 0
            # validar se vizinho x8 é valido. caso seja adicionar o seu valor a x8. caso nao seja x8=0
            if( isValid(i+1, j+1, len(m), len(m[i])) ):
                x8 = m[i+1][j+1]
            else:
                x8 = 0

            # soma dos valores dos vizinhos, com posições válidas
            m2[i][j] = soma(x1, x2, x3, x4, x5, x6, x7, x8)

    # envio do resultado pelo Pipe()
    pipe.send(m2)
    

if __name__ == "__main__":
    
    # dimensão do array (ex.: 1000x1000)
    d = 1000

    # criar array inicial, com valores aleatórios entre 0 e 9, de dimensão 1000x1000
    arr = np.random.random_integers(0, 9, (d,d))

    # pedir ao user o numero de processos
    num_processos = int(input("Numero de Processos: "))

    # verificar se o numero de processos é divisivel por 1000, para simplificar o processo de divisão do array
    while(d%num_processos != 0.0 ):
        num_processos = input("Insira um numero divisivel por 1000: ")

    # iniciar Pipes
    pipes = [ Pipe() for _ in range(num_processos) ]

    # passo inicial
    step = int(d/num_processos)
    
    # iniciar processos
    p = [
        mp.Process(target=alterMatrix, args=(arr[i * step: i* step + step], pipes[i][0],))
        for i in range(num_processos)
    ]
    
    [p.start() for p in p]

    # uso da matriz recebida pelo primeiro Pipe() para inicializar uma nova matriz M
    M = pipes[0][1].recv()

    # Concatenação das restantes matrizes, recebidas nos restantes Pipes, à matriz M
    for i in range(1, num_processos):
        m = pipes[i][1].recv()
        M = np.concatenate((M,m))
        
    [p.join() for p in p]

    # guardar resultados da matriz M num ficheiro
    with open("ex7.txt", "w") as file:
        for i in M:
            for j in i:
                file.write(str(j) + " ")

    print("Done")