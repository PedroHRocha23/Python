
import random
#Atlético x Cruzeiro
def geraMatriz(l, c):
    M = []
    for i in range(l):
        linha = []
        for j in range(c):
            x = random.randint(1, 3)
            linha.append(x)
        linha.sort()
        M.append(linha)
    return M



def main():
    l = int(input('Informe a quanridade de partidas:'))
    c = 2   
    

    vitoria_a = 0
    empate = 0
    vitoria_c = 0
    linha = geraMatriz(l, c)
    for i in range(len(linha)):
        if linha[i][0] > linha[i][1]:
            vitoria_a += 1
        elif linha[i][0] == linha[i][1]:
            empate += 1
        else:
            vitoria_c += 1

    print(linha)
    print(f'Vitórias do Atletico: {vitoria_a}\nVitórias do Cruzeiro: {vitoria_c}\nEmpates nos jogos: {empate}')
    if vitoria_a > vitoria_c:
        print('O Atlético é o melhor time')
    elif vitoria_c > vitoria_a:
        print('O Cruzeiro é o melhor time')
    else:
        print('Os times possuem a mesma quantidade de vitórias!')
main()