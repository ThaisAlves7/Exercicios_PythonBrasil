# Faça um programa que peça os 3 lados de um triangulo. O programa deverá informar se os valores podem ser um triangulo.
# Indique, caso os lados formem um triangulo, se o mesmo é: Equilatero, Isósceles ou Escaleno.
# Dicas:
    # 3 lados formam um triangulo quando a soma de quaisquer 2 lados for maior que o terceiro;
    # Triangulo Equilátero: 3 lados iguais;
    # Triangulo Isósceles: quaisquer dois lados iguais
    # Triangulo Escaleno: três lados diferentes;

lado_1 = float(input('Informe o 1° lado: '))
lado_2 = float(input('Informe o 2° lado: '))
lado_3 = float(input('Informe o 3° lado: '))

teste1 = lado_1 + lado_2
teste2 = lado_2 + lado_3
teste3 = lado_3 + lado_1

if ((teste1 < lado_3) or (teste2 < lado_1) or (teste3 < lado_2)):
    if ((lado_1 == lado_2) and (lado_1 == lado_3)):
        print('Isso é um Triângulo Equilátero')

    elif ((lado_1 == lado_2) or (lado_1 == lado_3) or (lado_2 == lado_3)):
        print('Isso é um Triângulo Isósceles')

    else:
        print('Isso é um Triângulo Escaleno')

else:
    print('Isso não é um Triângulo')

