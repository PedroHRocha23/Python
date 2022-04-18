
import random

def geraMatriz(l, c):
    M = []
    for i in range(l):
        linha = []
        for j in range(c):
            x = random.randint(1, 10)
            while verificarRepetido(x,linha) == True:
                x = random.randint(1, 10)
            linha.append(x)
        linha.sort()
        M.append(linha)

    return M
    

def avaliApostas(aposta, sorteados):
    cont = 0
    for i in range(len(aposta)):
        if aposta[i] == sorteados[i]:
            cont += 1
    if cont == 6:
        return True
    else:
        return False
    

def verificarRepetido(x,linha):
    cont = 0
    for i in range(len(linha)):
        if linha[i] == x:
            cont+=1
    if cont == 0:
        return False
    else:
        return True

def imprimeMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def main():
    linha = int(input('Linhas:'))
    coluna = 6 
    matriz = (geraMatriz(linha, coluna))
    imprimeMatriz(matriz)
    sorteados = [2,3,4,8,9,10]
    vet = []
    for i in range(len(matriz)):
        if avaliApostas(matriz[i], sorteados) == True:
            vet.append(i+1)
    print('Ganhadores',vet)

main()