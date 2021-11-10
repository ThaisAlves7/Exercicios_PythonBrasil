# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
# vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A
# frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia
# uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.


import unidecode

def conferir_igualdade(palavra):
    print(palavra[::-1])
    if str(palavra) == str(palavra)[::-1]:
        return print(f'Essa palavra é Palíndromo.')
    return print(f'Essa palavra não é Palíndromo.')


palavra1 = input('Informe uma palavra ou frase: ').lower().replace(' ', '').strip().replace('.', '')
palavra1 = unidecode.unidecode(palavra1)
conferir_igualdade(palavra1)
