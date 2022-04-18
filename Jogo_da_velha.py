#! python3.

tabuleiro = {'top-l':'','top-m':'','top-r':'','mid-l':'','mid-m':'','mid-r':'','low-l':'','low-m':'','low-r':''}

def ImprimeTabuleiro(tabuleiro):
    print(tabuleiro['top-l'] + '|' + tabuleiro['top-m'] + '|' + tabuleiro['top-r'])
    print('-+-+')
    print(tabuleiro['mid-l'] + '|' + tabuleiro['mid-m'] + '|' + tabuleiro['mid-r'])
    print('-+-+')
    print(tabuleiro['low-l'] + '|' + tabuleiro['low-m'] + '|' + tabuleiro['mid-r'])


def VerificaJogada(jogada, tabuleiro):
    ...
    #Em andamento
    

def ImprimeRegras():
    print('''
                                      INSTRUÇÕES PARA JOGAR

                1 - Existe apenas dois jogadores "X" ou "O" (não confunda com "0")
                2 - Digite o endereço de cada jogada como na figura abaixo:
                                           |       |
                                     top-l | top-m | top-r
                                      _____|_______|_____
                                           |       |
                                     mid-l | mid-m | mid-r
                                      _____|_______|_____
                                           |       |       
                                     low-l | low-m | low-r
                                           |       |
                    Copie exatamente como está na imagem senão seu jogo será reiniciado.
    ''')

def main():
    ImprimeRegras()
    flag = True
    while flag == True:

        jogador = input('Digite quem irá jogar na rodada: "X" ou "O": ').upper()
        posicao = input('''
        Escolha a posição da jogada
        
                                    |       |
                              top-l | top-m | top-r
                               _____|_______|_____
                                    |       |
                              mid-l | mid-m | mid-r
                               _____|_______|_____
                                    |       |       
                              low-l | low-m | low-r
                                    |       |

        Digite a posição: 
        ''')
        tabuleiro[posicao] = jogador
        ImprimeTabuleiro(tabuleiro)
        
        if tabuleiro['low-l'] == 'O' and tabuleiro['low-m'] == 'O' and tabuleiro['low-r'] == 'O'\
        or tabuleiro['low-l'] == 'X' and tabuleiro['low-m'] == 'X' and tabuleiro['low-r'] == 'X'\
        or tabuleiro['mid-l'] == 'O' and tabuleiro['mid-m'] == 'O' and tabuleiro['mid-r'] == 'O'\
        or tabuleiro['mid-l'] == 'X' and tabuleiro['mid-m'] == 'X' and tabuleiro['mid-r'] == 'X'\
        or tabuleiro['top-l'] == 'O' and tabuleiro['top-m'] == 'O' and tabuleiro['top-r'] == 'O'\
        or tabuleiro['top-l'] == 'X' and tabuleiro['top-m'] == 'X' and tabuleiro['top-r'] == 'X':
            print(f'Fim de jogo! Jogador {jogador} venceu!')
            flag = False

        elif tabuleiro['top-l'] == 'O' and tabuleiro['mid-l'] == 'O' and tabuleiro['low-l'] == 'O'\
        or   tabuleiro['top-m'] == 'O' and tabuleiro['mid-m'] == 'O' and tabuleiro['low-m'] == 'O'\
        or   tabuleiro['top-r'] == 'O' and tabuleiro['mid-r'] == 'O' and tabuleiro['low-r'] == 'O'\
        or   tabuleiro['top-l'] == 'X' and tabuleiro['mid-l'] == 'X' and tabuleiro['low-l'] == 'X'\
        or   tabuleiro['top-m'] == 'X' and tabuleiro['mid-m'] == 'X' and tabuleiro['low-m'] == 'X'\
        or   tabuleiro['top-r'] == 'X' and tabuleiro['mid-r'] == 'X' and tabuleiro['low-r'] == 'X':
            print(f'Fim de jogo! Jogador {jogador} venceu!')
            flag = False

        elif tabuleiro['top-l'] == 'O' and tabuleiro['mid-m'] == 'O' and tabuleiro['low-r'] == 'O'\
        or   tabuleiro['top-r'] == 'O' and tabuleiro['mid-m'] == 'O' and tabuleiro['low-l'] == 'O'\
        or   tabuleiro['top-l'] == 'X' and tabuleiro['mid-m'] == 'X' and tabuleiro['low-r'] == 'X'\
        or   tabuleiro['top-r'] == 'X' and tabuleiro['mid-m'] == 'X' and tabuleiro['low-l'] == 'X':
            print(f'Fim de jogo! Jogador {jogador} venceu!')
            flag = False

main()
