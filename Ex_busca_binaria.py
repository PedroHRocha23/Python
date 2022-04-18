
import random
import matplotlib.pyplot as plt 
import numpy as np

def PopulaVetor(x):
    vetor = [0]*x
    for i in range(len(vetor)):
        num = random.randint(1, len(vetor)*2)
        for j in range(len(vetor)):
            if num == vetor[j]:
                num = random.randint(1, len(vetor)*2)
                j = 0
        vetor[i] = num
    vetor.sort()
    return vetor
            
def buscaBinaria(vetor,x):
    cont=0
    low=0
    high=len(vetor)-1
    while low <= high:
        cont += 1
        mid = (low + high)//2
        if vetor[mid] == x:
            print("quantidade de passos--> ",cont)
            return mid
        else:
            if vetor[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
    print("quantidade de passos--> ",cont)
    return -1

def main():
    tamanho_vetor = [10,50,100,500,1000,5000,10000]
    for i in tamanho_vetor:
        print(f'Busca com {i} elementos:')
        (buscaBinaria(PopulaVetor(i), (i*2) + 1))

main()

#Gráfico
x = np.array([10,50,100,500,1000,5000,10000])  
y = np.array([4,6,7,9,10,13,14]) 
plt.xlabel('Tamanho do vetor')
plt.ylabel('Quantidade de repetições')
plt.plot(x, y)  
plt.show() 