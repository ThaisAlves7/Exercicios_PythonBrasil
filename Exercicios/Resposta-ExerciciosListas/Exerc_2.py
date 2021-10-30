# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa

lista_numeros = []

for i in range(1, 11):
    numbers = int(input(f'Informe {i}° numero: '))
    lista_numeros.append(numbers)

lista_numeros = sorted(lista_numeros, reverse=True)
print(f'Os números digitados foram: {lista_numeros}')