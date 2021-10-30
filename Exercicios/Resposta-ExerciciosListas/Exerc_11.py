# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

number_A, number_B, number_C = [], [], []
x, y = 1, 1

for i in range(1, 31):
    if i <= 10:
        num = int(input(f'Insira {i}° valor para Lista A: '))
        number_A.append(num)

    elif i <= 20:
        if i == 11:
            print()
        num = int(input(f'Insira {x}° valor para Lista B: '))
        number_B.append(num)
        x += 1

    else:
        if i == 21:
            print()
        num = int(input(f'Insira {y}° valor para Lista C: '))
        number_C.append(num)
        y += 1

number_D = number_A + number_B + number_C

print(f'A união das 3 lista é: {number_D}')