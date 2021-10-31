# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento
# for positivo, e ‘N’, se seu argumento for zero ou negativo

def positivo_negativo(num):
    if num <= 0:
        print('N')

    else:
        print('P')


number = float(input('Informe um numero e eu te retornarei se ele é Positivo(P) ou Negativo(N): '))
positivo_negativo(number)