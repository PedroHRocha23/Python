#~~~~~~~~~~~~~~~~~~~~~~~~CALCULADORA DE RESISTORES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Entrada de Dados
def Quantida_faixas(n):
    if n<3 or n>6:
        return 'Não existe resistor com esse número de faixas.'
    else:
        cores = ['']*n
        for i in range(n):
            cores[i] = input(f'Digite a cor da {i + 1}° faixa:')

        return cores
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Processamento de Informações:
def Tres_cores(lista_cores,cores,tolerancia):
    multiplicador = cores[lista_cores[2]] * '0'
    return str(cores[lista_cores[0]]) + str(cores[lista_cores[1]]) + multiplicador

def Quatro_cores(lista_cores,cores,tolerancia):
    multiplicador = cores[lista_cores[2]] * '0'
    return f'{str(cores[lista_cores[0]])}{str(cores[lista_cores[1]])}{multiplicador}\
    Tolerância: +/- {str(tolerancia[lista_cores[3]])}'

def Cinco_cores(lista_cores,cores,tolerancia):
    multiplicador = cores[lista_cores[3]] * '0'
    return f'{str(cores[lista_cores[0]])}{str(cores[lista_cores[1]])}{str(cores[lista_cores[2]])}{multiplicador}\
    Tolerância: +/- {str(tolerancia[lista_cores[4]])}'

def Seis_cores(lista_cores,cores,tolerancia,coef):
    if lista_cores[3] == 'dourado' or lista_cores[3] == 'prata':
        faixa1 = cores[lista_cores[0]]*100
        faixa2 = cores[lista_cores[1]]*10
        faixa_total = faixa1 + faixa2 + cores[lista_cores[2]]
        multiplicador = faixa_total * (cores[lista_cores[3]])

        return f'{multiplicador}\
        Tolerância: +/- {tolerancia[lista_cores[4]]}% ----> Coef.Temperatura: {str(coef[lista_cores[5]])} PPM/C'
    else:
        multiplicador = cores[lista_cores[3]] * '0'
        return f'{str(cores[lista_cores[0]])}{str(cores[lista_cores[1]])}{str(cores[lista_cores[2]])}{multiplicador}\
        Tolerância: +/- {str(tolerancia[lista_cores[4]])}% ----> Coef.Temperatura: {str(coef[lista_cores[5]])} PPM/C'
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Cores e Valores
cores = {
'preto':0,'marrom':1,'vermelho':2,'dourado':0.1,
'laranja':3,'amarelo':4,'verde':5,'azul':6,
'violeta':7,'cinza':8,'branco':9,'prata':0.01
}

tolerancia = {
'marrom':1,'vermelho':2,'verde':0.5,
'azul':0.25,'violeta':0.1,'cinza':0.05,
'dourado':5,'prata':10
}

coeficiente_temperatura = {
'marrom':100,'vermelho':50,'laranja':15,
'amarelo':25,'azul':10,'violeta':5
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    #Selecao_de_modo
    print('Quantas cores possue o resistor?'.rjust(50))
    modo = int(input('Digite aqui: '))
    lista_cores = Quantida_faixas(modo)
    print(lista_cores)

    if len(lista_cores) == 3:
        print(f'Valor: {Tres_cores(lista_cores, cores, tolerancia)}%')
    if len(lista_cores) == 4:
        print(f'Valor: {Quatro_cores(lista_cores, cores, tolerancia)}%')
    if len(lista_cores) == 5:
        print(f'Valor: {Cinco_cores(lista_cores, cores, tolerancia)}%')
    if len(lista_cores) == 6:
        print(f'Valor: {Seis_cores(lista_cores, cores, tolerancia, coeficiente_temperatura)}')
main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~