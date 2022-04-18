
def geraPolinomio(vet):
    polinomio = ''
    for i in range(len(vet) - 1,0,-1):
        polinomio += '' +str(vet[i]) + 'x^' + str(i) + ' + '
    polinomio += str(f' {vet[0]}')
    return polinomio

def calcula_polinomio(vet,x):

    exp = [None]*len(vet)
    calculo_polinomio =  [None]*len(vet)
    soma = 0
    for i in range(len(vet)):
        exp[i] = x**i  
    for j in range(len(vet)):
        calculo_polinomio[j] = vet[j] * exp[j]
        soma += calculo_polinomio[j]
    return soma
    
def soma_polinomios(vet1, vet2): 
    
    if len(vet1)>len(vet2):
        diferença = len(vet1) - len(vet2)
        menor = vet2
    else:
        diferença = len(vet2) - len(vet1)
        menor = vet1
    
    menor += [0]*diferença

    soma_pol = [0]*len(menor)
    
    for i in range(len(menor)):
        soma_pol[i] = vet1[i] + vet2[i]

    return geraPolinomio(soma_pol) 




def main():

    modo = input('Selecione a operação:\n1 - Calcular Polinômio\n2 - Soma de Polinômios\nOpção: ')
    if modo == '1':
        grau = int(input("grau do polinomio: "))
        base = int(input("Valor do 'x':"))
        grau +=1
        vet = [0]*grau
        for i in range(len(vet)-1, -1, -1):
            vet[i] = int(input("Digite o termo " + str(i) + ": "))
        print(geraPolinomio(vet))
        print(f'F(x) = {calcula_polinomio(vet, base)}')

    elif modo == '2':
        grau_1 = int(input('Grau do Primeiro polinômio:'))
        grau_2 = int(input('Grau do Segundo polinômio: '))
        grau_1 +=1
        grau_2 +=1
        vet1 = [0]*grau_1
        vet2 = [0]*grau_2
        for i in range(len(vet1)-1, -1, -1):
            vet1[i] = int(input("1° Polinômio --> Digite o termo " + str(i) + ": "))
        
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        for i in range(len(vet2)-1, -1, -1):
            vet2[i] = int(input("2° Polinômio --> Digite o termo " + str(i) + ": "))
        print(f'Soma: Polinômio 1 = {geraPolinomio(vet1)} + Polinômio 2 = {geraPolinomio(vet2)}')
        print(soma_polinomios(vet1, vet2))

inicio = input('Iniciar Calculadora:\n1-Começar\n0-Encerrar\nOpção:')
if inicio == 0:
    print('Volte Sempre!')
else:
    main()

while True:
    continuar = input('Deseja continuar?\nDigite --> S(sim) ou N(não):').lower()
    if continuar == 's':
        main()
    else:
        print('Volte sempre!')
        break
