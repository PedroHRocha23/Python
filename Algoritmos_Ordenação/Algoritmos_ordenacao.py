#Bibliotecas
import random
import time

#Função utilizada para verificar repetições em um vetor
def buscaBinaria(vetor, x):
    mid = len(vetor)//2
    if mid == 0:
        return False
    if vetor[mid] == x:
        return True
    else:
        if vetor[mid] < x:
            return buscaBinaria(vetor[mid:], x)
        elif vetor[mid] > x:
            return buscaBinaria(vetor[:mid], x)

#Cria um vetor de tamanho 'n' sem números repetidos.
def geraVetor(n):
    vetor = [0]*n
    for i in range(n):
        x = random.randint(1,n*2)
        while buscaBinaria(vetor,x) == True:
            x = random.randint(1, n * 2)
        vetor[i] = x
    return vetor

def Bubblesort(v):
    comp = 0
    mov = 0
    for k in range(len(v)):
        for i in range(len(v)-1-k):
            comp += 1
            if v[i] > v[i+1]:
                mov += 1 
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
    return comp, mov

def Selectionsort(v):
    comp = 0
    mov = 0
    for i in range(len(v)):
        min = i
        for j in range(i+1, len(v)):
            comp += 1
            if v[min] > v[j]:
                min = j
        mov += 1
        aux = v[i]
        v[i] = v[min]
        v[min] = aux
    return comp, mov

def Insertionsort(v):
    comp = 0
    mov = 0
    for i in range(1,len(v)):
        x = v[i]
        j = i - 1
        comp += 1 
        while j >= 0  and x < v[j]:
            v[j+1] = v[j]
            j -= 1
            mov += 1
        v[j+1] = x
        
    return comp, mov

def main():
    n = [100,1000,10000]

    for i in range(len(n)):
        vetor = geraVetor(n[i])
        print(vetor)
        A = vetor
        B = vetor
        C = vetor


        print(f'Tamanho do vetor --> {n[i]}')
        
        temp_ini_x = time.time()
        x,x1 = Bubblesort(A)
        temp_fim_x = time.time()

        print(f'Comparação:{x}   Movimentação:{x1}    tempo: {temp_fim_x - temp_ini_x}')
        
        temp_ini_x = time.time()
        y,y1 = Selectionsort(B)
        temp_fim_x = time.time()

        print(f'Comparação:{x}   Movimentação:{x1}    tempo: {temp_fim_x - temp_ini_x}')
        
        temp_ini_x = time.time()
        z,z1 = Insertionsort(C)
        temp_fim_x = time.time()

        print(f'Comparação:{x}   Movimentação:{x1}    tempo: {temp_fim_x - temp_ini_x}')
        
main()