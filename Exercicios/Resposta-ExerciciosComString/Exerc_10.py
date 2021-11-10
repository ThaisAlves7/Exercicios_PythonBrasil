# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por
# extenso.

from num2words import num2words


numero = int(input('Digite um numero: '))
numero_extenso = num2words(numero, lang='pt-br')

print(f'O numero {numero} por extenso é: {numero_extenso}')