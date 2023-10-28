#Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:
#
#1.	Somar
#2.	Multiplicar
#3.	Maior
#4.	Novos números
#5.	Sair do programa

menu = 0
x1 = 0
x2 = 0
x3 = 0


while True:
    menu = int(input('\nAgora escolha a opção a ser realizada:\n'
                     '[1] Somar\n'
                     '[2] Multiplicar\n'
                     '[3] Maior\n'
                     '[4] Novos números\n'
                     '[5] Sair do programa\n'))

    if menu == 1:
        print(f'\n{x1} + {x2} + {x3} = {x1+x2+x3}')
        break

    elif menu == 2:
        print(f'\n{x1} * {x2} * {x3} = {x1*x2*x3}')
        break

    elif menu == 3:
        maior = 0
        if x1 > x2 and x1 > x3:
            maior = x1
        if x2 > x1 and x2 > x3:
            maior = x2
        if x3 > x1 and x3 > x2:
            maior = x3

        print(f'\nO maior número é {maior}.')

    elif menu == 4:
        x1 = int(input('Digite o primeiro número: '))
        x2 = int(input('Digite o segundo número: '))
        x3 = int(input('Digite o terceiro número: '))

    elif menu == 5:
        print('\nFechando aplicação...')
        break