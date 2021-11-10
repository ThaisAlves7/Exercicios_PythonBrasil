# Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
        # F
        # U
        # L
        # A
        # N
        # O

def imprimir_vertical(palavra):
    caracteres_separados = list(palavra)
    for caracter in caracteres_separados:
        print(caracter)


texto = input('Informe seu nome e eu irie imprimi - lo na vertical: ').upper()
imprimir_vertical(texto)