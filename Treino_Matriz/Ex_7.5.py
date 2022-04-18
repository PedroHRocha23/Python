
def geraMatriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for i in range(n):
            x = int(input('Digite um valor:'))
            linha.append(x)
        matriz.append(linha)
    return matriz

def ImprimeMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def ProcessaCidade(linha):
    vetor = []
    for i in range(len(linha)):
        if linha[i] == 1:
            vetor += str(i+1)
    return vetor

def main():
    #matriz = [[0,1,1,0],[1,0,1,0],[1,1,0,1],[0,0,1,0]]  MATRIZ DE TESTE
    n = int(input('Informe o tamanho da matriz "N x N":'))
    matriz = geraMatriz(n)
    ImprimeMatriz(matriz)
    for i in range(len(matriz)):
        x = ProcessaCidade(matriz[i])
        print(f'A cidade {i+1} está conectada a outras {len(x)} cidades: {x}')

main()
