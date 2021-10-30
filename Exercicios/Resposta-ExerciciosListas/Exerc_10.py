# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão
# ser compostos pelos elementos intercalados dos dois outros vetores

number_A, number_B = [], []
x = 1

for i in range(1, 21):
    if i <= 10:
        num = int(input(f'Insira {i}° valor para Lista A: '))
        number_A.append(num)
    else:
        if i == 11:
            print()
        num = int(input(f'Insira {x}° valor para Lista B: '))
        number_B.append(num)
        x += 1

number_C = number_A + number_B

print(f'A união das 2 lista é: {number_C}')