
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
            
def buscaSequencialOrdenada(vetor,x):    
    for i in range(len(vetor)):        
        if vetor[i] == x:
            print("quantidade de passos--> ",i+1)
            return i
        else:
            if x < vetor[i]:
                print("quantidade de passos--> ",i+1)
                return -1
    print("quantidade de passos--> ",i+1)    
    return -1

def main():
    tamanho_vetor = [10,50,100,500,1000,5000,10000]
    for i in tamanho_vetor:
        print(f'Busca com {i} elementos:')
        (buscaSequencialOrdenada(PopulaVetor(i), (i*2) + 1))
    
main()

#Gráfico
x = np.array([10,50,100,500,1000,5000,10000])  
y = x 
plt.xlabel('Tamanho do vetor')
plt.ylabel('Quantidade de repetições')
plt.plot(x, y)  
plt.show() 