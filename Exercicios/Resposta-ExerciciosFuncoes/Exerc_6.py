# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter
# 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma
# para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as
# conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse
# cálculo para novos valores de entrada todas as vezes que desejar.


def converter_hora(tipo_conversao, hora, minuto):
    if tipo_conversao == 'A':
        hora = hora - 12

    else:
        hora = hora + 12

    saida_convertida(tipo_conversao, hora, minuto)


def saida_convertida(tipo_convertida, hora_convertida, minuto):
    if tipo_convertida == 'A':
        print(f'{hora_convertida}:{minuto} AM')

    else:
        print(f'{hora_convertida}:{minuto} PM')


print()
print('Convertendo HORA AM/PM ou PM/AM')
print()

continuar = ''

while continuar != 'N':
    tipo = input('Informe como deseja converter A - AM ou P - PM: ').upper()
    tipo = tipo[0]

    horas = int(input('Informe primeiro qual a HORA: '))
    valido = 0 <= horas <= 24
    while not valido:
        print()
        print('Informe uma hora valida entre 0 a 24')
        horas = int(input('Informe primeiro qual a HORA: '))
        valido = 0 <= horas <= 24
        print()

    minutos = int(input('Informe agora o MINUTO: '))
    valido = 0 <= minutos <= 59
    while not valido:
        print()
        print('Informe um minuto valido entre 0 a 59')
        minutos = int(input('Informe agora o MINUTO: '))
        valido = 0 <= minutos <= 59
        print()

    converter_hora(tipo, horas, minutos)

    continuar = input('Deseja converter mais Horas? S - Sim ou N - Não: ')[0].upper()
    valido = continuar in ['S', 'N']
    print()
    while not valido:
        print('Informe uma opção valida para continuar')
        continuar = input('Deseja converter mais Horas? S - Sim ou N - Não: ')[0].upper()
        valido = continuar in ['S', 'N']
        print()