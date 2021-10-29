# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo
    # termo.

fibonnaci = []

for n in range(1, 11):
    if n <= 1:
        fibonnaci.append(n)
    else:
        valor = (n - 1) + (n - 2)
        fibonnaci.append(valor)

print(fibonnaci)

