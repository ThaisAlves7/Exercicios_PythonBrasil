# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste
# conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.
# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133


numero = input('Informe o numero de telefone: ')
digitos = len(numero)


if digitos == 9 and '-' in numero:
    if numero[4] == '-':
        print('O numero esta certo')

    else:
        numero = numero.replace('-', '')
        num_valido = numero[:4]+'-'+numero[4:]
        print(num_valido)

elif digitos > 8:
    if '-' in numero:
        numero = numero.replace('-', '')
    ultimo = numero
    while digitos > 9:
        ultimo = ultimo[:-1]
        digitos = len(ultimo)
        print(456)

    num_valido = ultimo[:4]
    num_valido += '-'+ultimo[4:]
    print(num_valido)

else:
    if '-' in numero:
        numero = numero.replace('-', '')
    ultimo = ''
    digitos = len(numero)+len(ultimo)
    while digitos < 8:
        ultimo += '3'
        digitos = len(numero)+len(ultimo)
        # print(ultimo)

    ultimo += numero
    num_valido = ultimo[:4] + '-' + ultimo[4:]
    print(num_valido)
