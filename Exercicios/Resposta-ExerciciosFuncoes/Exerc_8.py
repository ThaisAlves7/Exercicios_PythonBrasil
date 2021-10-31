# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contar_digitos(numero):
    palavra = str(numero)
    digitos = len(palavra)
    print(f'O número {numero} tem {digitos}')

num = int(input('Informe um numero inteiro: '))
contar_digitos(num)