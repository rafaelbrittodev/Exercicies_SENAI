#Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico,
#permitindo que o usuário faça depósitos, saques e consulte o saldo da conta, e sair
import math

menu = ''
saldo = 0

while True:
    print(f'\n********** CAIXA ELETRÔNICO **********\n'
          f'[1] Consultar saldo em conta corrente.\n'
          f'[2] Depositar valor\n'
          f'[3] Realizar saque\n'
          f'[4] Sair')

    menu = int(input('\n'))

    if menu == 1:
        print(f'Seu saldo é de R$ {saldo:.2f}')

    elif menu == 2:
        deposito = float(input('Digite o valor que deseja depositar: \nR$ '))
        saldo = saldo + deposito

    elif menu == 3:
        print('Notas disponíveis: 2, 5 , 10, 20, 50, 100, 200\n')

        saque = int(input('Digite o valor que deseja sacar: '))
        if saque <= saldo:
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
                                            print(f'\nSacando {math.floor(nota2)} cédula de R$ 2')
            print(f'Valor total de saque R$ {saque:.2f}')
            saldo = saldo - saque
        else:
            print(f'\nSaldo indisponível, seu saldo atual é de R$ {saldo:.2f}')

    elif menu == 4:
        print('Saindo ...')
        break

