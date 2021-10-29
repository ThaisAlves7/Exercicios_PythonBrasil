# Faça um programa que calacule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles
    # O usuario deverá informar a quantidade de CDs e o valor para cada um


qtde_cd = []
valor_cd = []
cont = 1

continuar = 1
cd = int(input('Informe a quantidade de CDs: '))
qtde_cd.append(cd)
valor = float(input('Informe o valor pago por apenas 1 modelo do CD: '))
valor_cd.append(valor)
print()

while continuar != 2:
    continuar = int(input('Deseja continuar 1 - Sim e 2 - Não: '))
    print()
    if continuar == 1:
        cd = int(input('Informe a quantidade de CDs: '))
        qtde_cd.append(cd)
        valor = float(input('Informe o valor pago por apenas 1 modelo do CD: '))
        valor_cd.append(valor)
        print()

for i, j in zip(qtde_cd, valor_cd):
    media = j / i
    print(j, i)
    print(f'O valor média da {cont}° é {media:.2f}')
    cont += 1
