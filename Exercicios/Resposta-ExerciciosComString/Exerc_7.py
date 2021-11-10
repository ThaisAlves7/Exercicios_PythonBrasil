# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
    # a. quantos espaços em branco existem na frase.
    # b. quantas vezes aparecem as vogais a, e, i, o, u.


vogais = ['a', 'e', 'i', 'o', 'u']

def contar_caracter(palavra):
    count_vogais = 0
    list_palavra = list(palavra)
    espacos = palavra.count(' ')
    for caracter in list_palavra:
        if caracter in vogais:
            count_vogais += 1

    print(f'A frase "{palavra}", possui {espacos} em brancos')
    print(f'A frase "{palavra}", possui {count_vogais} vogais')

contar_caracter('a bac axi  roxo')