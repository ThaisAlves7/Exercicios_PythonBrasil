#Encontrar número primos é um tarefa dificil. Faça um programa que gera uma lista dos numeros primos existentes entre 1
    # e um numero informado pelo usuario.

def validar_numeros_primos(number):
    cont = 1
    primos = []


    while number != 0:
        for i in range(1, number):
            if (number % i == 0):
                cont += 1

        if (cont == 2):
            primos.append(number)

        number -= 1
        cont = 1
    print(sorted(primos))

num = int(input('Digite um número: '))

if ((num < 0) or (num == 1)):
    print(f'O número {num} não é um número válido')

else:
    validar_numeros_primos(num)