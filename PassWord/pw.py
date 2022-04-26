#! python3
#pw.py - Um programa para repositório de senhas que não é seguro

import sys
import pyperclip as pc

def AdicionarSenha(repositório):
    nova_senha = input('Digite a nova senha: ')
    referencia = input('Digite uma referência para a nova senha: ')
    repositório.setdefault(referencia,nova_senha)
    print('Senha adicionada')
    return repositório

senha = {'mackenzie':'654321', 'drive': '123456'}

if len(sys.argv) < 2:
    print('O comando deve ter um argumento\n \'python pw.py "conta desejada"')
    sys.exit()

conta = sys.argv[1]
if conta in senha:
    pc.copy(senha[conta])
    print(f'Senha de {conta} foi copiada para a área de transferência')
    sys.exit()
else:
    print('Senha não cadastrada no sistema!\n')
    cadastro = input('Deseja cadastrar uma nova senha?')
    if cadastro == 'sim':
        AdicionarSenha(senha)
        sys.exit()
    else:
        print('Ok :)')
        sys.exit()