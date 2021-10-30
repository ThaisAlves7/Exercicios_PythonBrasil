# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vogais = ['A', 'E', 'I', 'O', 'U']
consoantes = []
cont = 0

for i in range(1, 12):
    palavra = input('Insira uma caracter: ').upper()
    palavra = palavra[0]
    if palavra not in vogais:
        consoantes.append(palavra)
        cont += 1

print(f'Foram lidas {cont} consoantes que são: {consoantes}')