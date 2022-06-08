import random
from random import sample
import time

def apresentacao():
    print(r'''
  ____ ___  ___ ____  __ __    __  __  ___     ____   ___  __     ___  __ __ ____   ___   __ 
 ||    ||\\//|| || \\ || ||    ||  || // \\    || \\ // \\ ||    // \\ || || || \\ // \\ (( \
 ||==  || \/ || ||_// || ||    ||==|| ||=||    ||_// ||=|| ||    ||=|| \\ // ||_// ||=||  \\ 
 ||___ ||    || ||    || ||__| ||  || || ||    ||    || || ||__| || ||  \V/  || \\ || || \_))

                        --> O jogo possui 5 rodadas
                        --> 2 jogadores
                        --> Vocês tem 5 segundos para pensar na resposta
                        --> Digitar a resposta apenas quando os dois tiverem pensado na resposta
    ''')

def selecionaTema(temas):
    num_tema = random.randint(0, len(temas) - 1)
    tema = temas[num_tema]
    return tema

def loopGame(temas):
    jogador1 = []
    jogador2 = []
    temas_selecionados = sample(temas, 5)
    for i in range(len(temas_selecionados)):
        print(f'\nTema da Rodada: {temas_selecionados[i]}')
        time.sleep(5)
        jogador1 += input('JOGADOR 1 --> Digite a maior palavra possível: ')
        jogador2 += input('\nJOGADOR 2 --> Digite a maior palavra possível: ')
    
    print(f'\nQuantidade de letras jogador 1: {len(jogador1)}')
    print(f'Quantidade de letras jogador 2: {len(jogador2)}')
    if len(jogador1) > len(jogador2):
        print('\nJOGADOR 1 VENCEU!!!')
    elif len(jogador1) < len(jogador2): 
        print('\nJOGADOR 2 VENCEU!!!')
    else:
        print('\nEMPATOU!!!')
def main():
    apresentacao()
    temas = ['fruta','nome','carro','pais','objeto','cor','animal','time de futebol']
    inicio = int(input('Deseja iniciar?\n1 - Sim\n0 - Não\nDigite:'))
    if inicio == 1:
        loopGame(temas)
    else:
        print('JOGUE QUANDO QUISER!!!')
main()