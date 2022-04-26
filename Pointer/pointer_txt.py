#Acrescenta marcadores a palavras em um arquivo txt (tem que rodar no cmd)

import sys
import pyperclip as pc

texto = sys.argv[1] 

arquivo = open(f'{texto}','r',encoding='utf-8')

linhas = []
linha_vazia = ''
while True:
    linha = arquivo.readline().rstrip()
    if linha == linha_vazia:
        break
    else:
        linhas.append(linha)

linha_com_marcadores = []
for i in linhas:
    linha_com_marcadores.append('* ' + i)

texto_marcado = ''
for i in linha_com_marcadores:
    texto_marcado += i + '\n'

pc.copy(texto_marcado)
print('Texto copiado para a área de tranferência.')
sys.exit()