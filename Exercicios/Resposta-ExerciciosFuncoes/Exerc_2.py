#  Faça um programa para imprimir:
#  1
#  1 2
#  1 2 3
#  .....
#  1 2 3 ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def escadinha_proximo_na_escada(num):
    if isinstance(num, int):
        if isinstance(num, int):
            x = 1
            while x <= num:
                y = 1
                escadinha = ''
                while y <= x:
                    escadinha += str(y) + ' '
                    y += 1
                print(escadinha)
                x += 1



number = int(input('Informe o numero da repetição para realizar a escadinha de numeros: '))
escadinha_proximo_na_escada(number)