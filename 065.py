# Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo e uma lista. No final mostre:
#
# 1. Quantas pessoas foram cadastradas
# 2. Uma listagem com as pessoas com o maior QI
# 3. Uma listagem com as pessoas de menor QI

list = [[],[]]
i = 0

while True:
    try:
        menu = int(input(f'[1] Cadastrar pessoa\n'
                     f'[2] Imprimir cadastros\n'
                     f'[3] Sair\n'))

        if menu == 1:
            nome = input('Digite o nome: ')
            qi = int(input('Digite o número do QI: '))
            list[0].append(nome)
            list[1].append(qi)

        elif menu == 2:
            print(f'\nForam cadastrados {len(list[0])} pessoas.'
                  f'\nA pessoa com maior QI é {list[0][list[1].index(max(list[1]))]}'
                  f'\nA pessoa com menor QI é {list[0][list[1].index(min(list[1]))]}\n')

        elif menu == 3:
            print('Saindo...')
            break

    except ValueError:
        print('Opção inválida, tente novamente.')