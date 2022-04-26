#Acrescenta marcadores a palavras de um texto que esta na area de tranferência do usuário

import pyperclip as pc

texto = pc.paste()
linhas = texto.split('\n')
linhas_marcadas = []
for i in linhas:
    linhas_marcadas.append('* ' + i)
texto_marcado = ''
for i in linhas_marcadas:
    texto_marcado += i + '\n'

pc.copy(texto_marcado)
print('Texto copiado para a área de Transferência')