# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de
# combustível. Calcule e mostre:
 # a. O modelo do carro mais econômico;
 # b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000
 # quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de
 # exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem
 # mudar a cada execução do programa.
 # Comparativo de Consumo de Combustível
   # Veículo 1
   # Nome: fusca
   # Km por litro: 7
   # Veículo 2
   # Nome: gol
   # Km por litro: 10
   # Veículo 3
   # Nome: uno
   # Km por litro: 12.5
   # Veículo 4
   # Nome: Vectra
   # Km por litro: 9
   # Veículo 5
   # Nome: Peugeout
   # Km por litro: 14.5
 # Relatório Final
 #  1 - fusca - 7.0 - 142.9 litros - R$ 321.43
 #  2 - gol - 10.0 - 100.0 litros - R$ 225.00
 #  3 - uno - 12.5 - 80.0 litros - R$ 180.00
 #  4 - vectra - 9.0 - 111.1 litros - R$ 250.00
 #  5 - peugeout - 14.5 - 69.0 litros - R$ 155.17
 # O menor consumo é do peugeout.


modelo_carros = ['Fusca', 'Gol', 'Uno', 'Vectra', 'Peugeout']
consumo = [7, 10, 12.5, 9, 14.5]
litros_gastar, custo_total = [], []
km_que_deseja_rodar = 1000
gasolina = 2.25



def calculo_consumo(km_rodar, preco_gasolina, consumo_litro):
 litro_necessario = km_rodar / consumo_litro
 litro_necessario = round(litro_necessario, 2)

 preco_a_pagar = litro_necessario * preco_gasolina
 preco_a_pagar = round(preco_a_pagar, 2)

 litros_gastar.append(litro_necessario)
 custo_total.append(preco_a_pagar)


print('Comparativo de Consumo de Combustível')
print()
for km_litro in consumo:
    calculo_consumo(km_que_deseja_rodar, gasolina, km_litro)


i, maior, menor = 1, 1, 9999
for modelo, litro_km in zip(modelo_carros, consumo):
    print(f'Veiculo {i}\n'
          f'Nome: {modelo}\n'
          f'Km por Litro: {litro_km}')

    espaco = len(modelo)
    if espaco > maior:
        maior = espaco

    i += 1

i = 1
print('Relatório Final')
for modelo, litro_km, litro_necessario, valor_paga in zip(modelo_carros, consumo, litros_gastar, custo_total):
    print(f'{i} - {modelo.ljust(maior)} - {str(litro_km).ljust(maior)}- {litro_necessario} litros\t-\tR${valor_paga}')
    i += 1

    if litro_necessario < menor:
        menor = litro_necessario
        menor_consumo = modelo
print()
print(f'O menor consumo é do {menor_consumo}')