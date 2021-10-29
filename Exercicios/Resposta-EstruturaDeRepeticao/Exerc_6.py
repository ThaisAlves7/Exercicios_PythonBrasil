# Faça um programa que imprima na tela os numero de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele
 # mostre os numeros um ao lado do outro

valores = []
for i in range(1, 21):
    valores.append(i)

for i in range(len(valores)):
    print(f'{valores[i]}')

print(valores)