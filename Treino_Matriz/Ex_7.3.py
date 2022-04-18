
import random

def geraMatriz():
    linhaEcoluna = random.randint(3, 5)

    matriz = []
    for i in range(linhaEcoluna):
        linha = [0]*linhaEcoluna
        for j in range(linhaEcoluna):
            linha[j] = random.randint(0, 1)
        matriz.append(linha)
    return matriz

def ImprimeMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def DimensaoMatriz(matriz):
    num = len(matriz)
    return f'Dimensão da Matriz {num}x{num}'

def TriangularSuperior(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i > j and matriz[i][j] != 0:
                return 'A matriz não é triangular superior'
    return 'A matriz é triangular superior'

def main():
    matriz = geraMatriz()
    ImprimeMatriz(matriz)
    print(DimensaoMatriz(matriz))
    print(TriangularSuperior(matriz))


main()
