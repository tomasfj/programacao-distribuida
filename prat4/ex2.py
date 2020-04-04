'''
F1
 - ler linhas de um file
 - colocar linha na queue

F2
 - tira linha da queue
 - converte linha para maiuscula
 - guarda num file 
'''

import multiprocessing
import time
import base64

# codificar e descodificar usando Vigenere cipher 
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def lerFile(lusiadas, key):
    f_in = open("ex2_in.txt", "r")

    for line in f_in:
        lusiadas.put(encode(key, line))
    
    lusiadas.put(encode(key, "done"))
    
    f_in.close()

def escreverFile(lusiadas, key):
    f_out = open("ex2_out.txt", "w")

    while True:
        line = decode(key, lusiadas.get())
        
        if(line== "done"):
            break

        f_out.write(line)
    
    f_out.close()

def ler_sequencial(key):
    fs_in = open("ex2_in.txt", "r")
    lista = []

    for line in fs_in:
        lista.append(encode(key, line))

    fs_in.close()

    return lista

def escreve_sequencial(key, lista):
    fs_out = open("ex2_out.txt", "w")

    for line in lista:
        fs_out.write(decode(key, line))

    fs_out.close()

def versao_sequencial(key):
    fs_in = open("ex2_in.txt", "r")
    fs_out = open("ex2_out.txt", "w")

    for line in fs_in:
        encoded_line = encode(key, line)
        decoded_line = decode(key, encoded_line)
        fs_out.write(decoded_line)

    fs_in.close()
    fs_out.close()

if __name__ == "__main__":
    lusiadas = multiprocessing.Queue()
    key = "password"

    start = time.time()

    p1 = multiprocessing.Process(target = lerFile, args= ((lusiadas),key))
    p2 = multiprocessing.Process(target = escreverFile, args = ((lusiadas),key))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Processos Execution time = %s" %(time.time()-start))

    # sequencial
    start = time.time()
    #versao_sequencial(key)
    lista = ler_sequencial(key)
    escreve_sequencial(key, lista)
    print("Sequencial Execution time = %s" %(time.time()-start))


'''
Resultados obtidos:
Processos Execution time = 0.012457847595214844
Sequencial Execution time = 0.0024034976959228516

Análise:
Os resultados obitdos mostram um tempo de execução menor para a forma 
sequencial.
'''