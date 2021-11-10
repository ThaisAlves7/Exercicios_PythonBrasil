# Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
    # F
    # FU
    # FUL
    # FULA
    # FULAN
    # FULANO


def escada_caracter(palavra):
    list_palavra = list(palavra)
    texto = ''
    for caracter in list_palavra:
        texto += caracter
        print(texto)

frase = input('Insira seu nome eu montarei uma escada com ele: ').upper()
escada_caracter(frase)