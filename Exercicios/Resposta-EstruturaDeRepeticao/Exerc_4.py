# Suponho que a população de um país A seja da ordem de 80000 habiteantes com uma taxa anual de crescimento de 3% e que
    # a população B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o numero
    # de anos necessarios para que a população do Pais A ultrapasse ou iguale a população do Pais B, mantidas as taxas de crescimento

pais_A, pais_B, cont_anos = 80000, 200000, 0

cresc_A, cresc_B = 3, 1.5

validar = True if (pais_A >= pais_B) else False

while (validar != True):
    pais_A = pais_A + ((pais_A * cresc_A) / 100)
    pais_B = pais_B + ((pais_B * cresc_B) / 100)
    cont_anos += 1
    validar = True if (pais_A >= pais_B) else False

print(f'O pais A vai ultrapassar o Pais B em {cont_anos} anos.')