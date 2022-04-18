
def populaMatriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            x = float(input('Digite um valor:'))
            linha.append(x)
        matriz.append(linha)
    return matriz

def ImprimeMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def Diagonal(matriz):
    vetor = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                vetor.append(matriz[i][j])
    return vetor

def TracoMatriz(vetor):
    soma = 0
    for i in vetor:
        soma += i
    return soma 

def numNulos(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if not(i == j) and matriz[i][j] == 0:
                soma += 1
    return soma

def main():
    n = int(input('Digite o tamanho da matriz:'))
    matriz = populaMatriz(n)
    ImprimeMatriz(matriz)
    vetor = Diagonal(matriz)
    print(f'Elementos da Diagonal: {vetor}')
    traco = TracoMatriz(vetor)
    print(f'Traço da Matriz: {traco}')
    nulos = numNulos(matriz)
    print(f'Número de Elementos fora da diagonal principal: {nulos}')


main()

