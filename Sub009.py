#Simulador de Caixa Eletrônico
#Simule um caixa eletrônico. Primeiro pergunte ao usuário qual valor ele quer retirar, depois dê o dinheiro com o menor número possível de notas.
import math

print('--------------- CAIXA ELETRÔNICO ---------------\n'
      'Notas disponíveis: 2, 5 , 10, 20, 50, 100, 200\n')

saque = int(input('Digite o valor que deseja sacar: '))

if saque % 200 >= 0:
    nota200 = saque / 200
    saque_atual = saque % 200
    if nota200 >= 1:
        print(f'Sacando {math.floor(nota200)} cédula de R$ 200')

    if saque_atual % 100 >= 0:
        nota100 = saque_atual / 100
        saque_atual = saque_atual % 100
        if nota100 >= 1:
            print(f'Sacando {math.floor(nota100)} cédula de R$ 100')

        if saque_atual % 50 >= 0:
            nota50 = saque_atual / 50
            saque_atual = saque_atual % 50
            if nota50 >= 1:
                print(f'Sacando {math.floor(nota50)} cédula de R$ 50')

            if saque_atual % 20 >= 0:
                nota20 = saque_atual / 20
                saque_atual = saque_atual % 20
                if nota20 >= 1:
                    print(f'Sacando {math.floor(nota20)} cédula de R$ 20')

                if saque_atual % 10 >= 0:
                    nota10 = saque_atual / 10
                    saque_atual = saque_atual % 10
                    if nota10 >= 1:
                        print(f'Sacando {math.floor(nota10)} cédula de R$ 10')

                    if saque_atual % 5 >= 0:
                        nota5 = saque_atual / 5
                        saque_atual = saque_atual % 5
                        if nota5 >= 1:
                            print(f'Sacando {math.floor(nota5)} cédula de R$ 5')

                        if saque_atual % 2 >= 0:
                            nota2 = saque_atual / 2
                            saque_atual = saque_atual % 2
                            if nota2 >= 1:
                                print(f'Sacando {math.floor(nota2)} cédula de R$ 2')

print(f'Valor total de saque R$ {saque:.2f}')