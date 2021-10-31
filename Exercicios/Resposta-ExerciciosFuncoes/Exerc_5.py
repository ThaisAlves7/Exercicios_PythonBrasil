# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a
# quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função
# “altera” o valor de custo para incluir o imposto sobre vendas.


def somaImposto(custo, taxaImposto):
    custo = custo + ((custo * taxaImposto) / 100)
    return print(f'O valor com taxa é R${custo:.2f}')


preco = float(input('Informe o valor de custo R$ '))
taxa = float(input('Informe o valor da Taxa: '))
somaImposto(preco, taxa)

