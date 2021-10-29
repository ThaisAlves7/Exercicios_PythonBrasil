# Faça um programa que leia 5 numeros e informe o maior número

valores = []

for i in range(1, 6):
    number = int(input(f'Informe {i}° número: '))
    valores.append(number)

print(f'O maior numero digitado foi {max(valores)}')