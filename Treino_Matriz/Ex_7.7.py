
def VerificaEstoque(produtos,minimo,estoque):
    texto = ''
    for i in range(len(produtos)):
        if estoque[i] < minimo[i]:
            texto += f'Produto: {produtos[i]} - Faltam {minimo[i] - estoque[i]} unidades.\n'
    return texto

def main():
    produtos = ['HD','Impressora','Monitor','Notebook','Tablet']
    minimo = [100,40,50,30,80]
    estoque = [[42,48,32,32,81],[102,38,50,15,85],[100,40,50,30,80],[100,40,50,35,78]]

    texto = ''
    for i in range(len(estoque)):
        x = VerificaEstoque(produtos, minimo, estoque[i])
        print(f'Loja {i+1}')
        if x == texto:
            print(f'- Todos os produtos possuem o estoque mínimo\n')
        else:
            print(x)

main()
