#criar matriz
import random

def CriaMatriz(l, c):
    M = []
    for i in range(l):
        linha = []
        for j in range(c):
            linha.append(random.randint(1, 100))
        M.append(linha)
    return M

def ImprimeMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])



def main():
    lin = int(input('linhas:'))
    col = int(input('colunas:'))
    M= CriaMatriz(lin, col)
    ImprimeMatriz(M)

main()
