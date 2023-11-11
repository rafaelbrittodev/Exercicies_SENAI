#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final mostre:
#
#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000,00
#Qual é o produto mais barato

total = 0
maior = 0
soma = 0
menor_name = ''
menor = None

while True:
    menu = int(input(f'\n***** Carinho de compras *****\n'
                        f'[1] Adicionar novo produto\n'
                        f'[2] Finalizar compra\n'
                        f'[3] Sair\n'))

    if menu == 1:
        new_name = str(input('\nDigite o nome do produto: '))
        new_valor = float(input('\nDigite o seu valor: R$ '))
        total += new_valor

        if menor == None or new_valor < menor:
            menor = new_valor
            menor_name = new_name

        if new_valor >= 1000:
            maior += 1

    elif menu == 2:
        print(f'\nO valor total da compra é R$ {total:.2f}\n'
              f'o número de produtos acima de  R$ 1000.00 foram {maior}\n'
              f'O produto mais barato foi {menor_name.upper()} custando R$ {menor:.2f}\n')

    elif menu == 3:
        print(f'\nSaindo ...')
        break

