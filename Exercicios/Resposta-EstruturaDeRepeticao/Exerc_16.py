# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até
# que o valor seja maior que 500

fibonnaci = []
limite = True
n = 0

while limite:
    for n in range(1, 10000):
        if n <= 1:
            valor = n
            fibonnaci.append(valor)
        else:
            valor = (n - 1) + (n - 2)
            fibonnaci.append(valor)

        if valor > 500:
            limite = False
            break

print(fibonnaci)

