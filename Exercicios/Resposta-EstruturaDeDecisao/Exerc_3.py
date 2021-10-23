# Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M- Masculino, Sexo Inválido

sexo = input('Informe o seu sexo F ou M: ').strip()
sexo = sexo.capitalize()

if (sexo == 'F'):
    print(f'O sexo digitado foi {sexo} - Feminino')

elif (sexo == 'M'):
    print(f'O sexo digitado foi {sexo} - Masculino')

else:
    print('Sexo Inválido')