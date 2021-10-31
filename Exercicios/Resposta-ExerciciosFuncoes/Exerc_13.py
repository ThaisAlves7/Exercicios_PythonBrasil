# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘.
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o
# valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser
# modificados para valores dentro da faixa de forma elegante.

def validar_omissao(valor):
    if valor == '':
        return 1

    else:
        return minimo_maximo(int(valor))

def minimo_maximo(valor):
    if valor < 1:
        return 1

    elif valor > 20:
        return 20

    else:
        return valor

def criar_linha(linha):
    line = '+'
    for x in range(linha):
        line += '-'
    line += '+'
    print(line)

def criar_coluna(linha, coluna):
    for y in range(coluna):
        c = '|'
        c += ' ' * linha
        c += '|'
        print(c)

def desenhar_moldura(linha, coluna):
    criar_linha(linha)
    criar_coluna(linha, coluna)
    criar_linha(linha)

line = input('Informe quantos +---------+, entre 1 e 20 você deseja: ')
column = input('Informe quantos |        |, entre 1 e 20 você deseja: ')

desenhar_moldura(validar_omissao(line), validar_omissao(column))