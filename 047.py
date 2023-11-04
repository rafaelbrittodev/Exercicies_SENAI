#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
#e o programa vai informar quantas cédulas de cada valor serão entregues.
#
#Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

import math

print('--------------- CAIXA ELETRÔNICO ---------------\n'
      'Notas disponíveis: 1, 10, 20, 50\n')

saque = int(input('Digite o valor que deseja sacar: '))

if saque % 50 >= 0:
    nota50 = saque / 50
    saque_atual = saque % 50
    if nota50 >= 1:
        print(f'Sacando {math.floor(nota50)} cédula de R$ 50')

    if saque_atual % 20 >= 0:
        nota20 = saque_atual / 20
        saque_atual = saque_atual % 20
        if nota20 >= 1:
            print(f'Sacando {math.floor(nota20)} cédula de R$ 20')

        if saque % 10 >= 0:
            nota10 = saque / 10
            saque_atual = saque % 10
            if nota10 >= 1:
                print(f'Sacando {math.floor(nota10)} cédula de R$ 10')

            if saque_atual % 1 >= 0:
                nota1 = saque_atual / 1
                saque_atual = saque_atual % 1
                if nota1 >= 1:
                    print(f'Sacando {math.floor(nota1)} cédula de R$ 1')



print(f'\nValor total de saque R$ {saque:.2f}')