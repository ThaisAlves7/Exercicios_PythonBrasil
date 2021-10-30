# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade
# e a altura na ordem inversa a ordem lida.

lista_idade, lista_altura = [], []

for i in range(1, 6):
    idade = int(input('Informe a idade: '))
    lista_idade.append(idade)

    altura = float(input('Informe sua altura: '))
    lista_altura.append(altura)
    print()

reverso_idade = list(reversed(lista_idade))
reverso_altura = list(reversed(lista_altura))

print(f'A lista invertida da idade é: {reverso_idade}')
print(f'A lista invertida da idade é: {reverso_altura}')
