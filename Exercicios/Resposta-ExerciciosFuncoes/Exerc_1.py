# Faça um programa para imprimir:
#  1
#  2 2
#  3 3 3
#  .....
#  n n n n n n ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha

def escadinha(num):
    for i in range(1, num+1):
        print(f'{i} '* i)


number = int(input('Informe o numero da repetição para realizar a escadinha de numeros: '))
escadinha(number)