# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(num):
    palavra = str(num)
    palavra_reverso = palavra[::-1]
    print(f'O numero {num} invertido é {palavra_reverso}')


numero = int(input('Informe um numero: '))
reverso(numero)

