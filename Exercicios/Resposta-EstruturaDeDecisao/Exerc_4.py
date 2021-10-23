# Faça um programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ['A', 'E', 'I', 'O', 'U']

letra = input('Digite uma letra: ').strip()
letra = letra.capitalize()

if letra in vogais:
    print(f'A letra {letra} é uma vogal')
else:
    print(f'A letra {letra} é uma consoante')