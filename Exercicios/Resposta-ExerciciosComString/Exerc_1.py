# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe
# também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
# Compara duas strings
    # String 1: Brasil Hexa 2006
    # String 2: Brasil! Hexa 2006!
    # Tamanho de "Brasil Hexa 2006": 16 caracteres
    # Tamanho de "Brasil! Hexa 2006!": 18 caracteres
    # As duas strings são de tamanhos diferentes.
    # As duas strings possuem conteúdo diferente.

import unidecode

def conferir_igualdade(palavra1, palavra2):
    texto1 = set(palavra1.split())
    texto2 = set(palavra2.split())
    if texto1 != texto2:
        return print(f'As duas strings possuem conteúdo diferente.')
    return print(f'As duas strings possuem conteúdo iguais.')

def contagem_caracter(palavra1, palavra2):
    tamanho1 = len(palavra1)
    tamanho2 = len(palavra2)
    if tamanho1 != tamanho2:
        return print('As duas strings são de tamanhos diferentes')
    return print('As duas strings são de tamanhos iguais')


def exibir_informacao(string1, string2):
    print(f'String 1: {string1}')
    print(f'String 2: {string2}')
    print(f'Tamanho de "{string1}": {len(string1)} caracteres')
    print(f'Tamanho de "{string2}": {len(string2)} caracteres')
    conferir_igualdade(string1, string2)
    contagem_caracter(string1, string2)


palavra1 = input('Informe uma palavra ou frase: ').title()
palavra1 = unidecode.unidecode(palavra1)
palavra2 = input('Informe outra palavra ou frase: ').title()
palavra2 = unidecode.unidecode(palavra2)

exibir_informacao(palavra1, palavra2)

