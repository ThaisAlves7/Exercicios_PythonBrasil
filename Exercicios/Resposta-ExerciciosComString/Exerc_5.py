# Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
# FULANO
# FULAN
# FULA
# FUL
# FU
# F


def escada_reversa(palavra):
    list_palavra = list(palavra)
    texto = palavra
    for caracter in reversed(list_palavra):
        print(texto)
        texto = texto.replace(caracter, '')


frase = input('Informe uma palavra ou frase: ').upper()
escada_reversa(frase)