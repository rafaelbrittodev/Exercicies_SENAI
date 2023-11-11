#Crie um programa para jogar par ou ímpar com o usuário,
#e só pare quando perder. Ao final deve mostrar a quantidade de vitórias

import random

PC = random.randint(1,2)
i = 0

print(f'***** Game par ou impar *****\n')

while True:
    user_1 = int(input(f'Faça sua escolha:\n'
                       f'[1] para impar.\n'
                       f'[2] para par.\n'))

    user_2 = int(input(f'Escolha:\n'
                       f'[1] Um.\n'
                       f'[2] Dois.\n'))


    if user_1 == 1:
        if user_2 == 1 and PC == 1:
            print(f'\nVocê perdeu para a máquina, o resultado foi par.\nEscolha PC: {PC}')
            print(f'Quantidade de vitórias nº {i}')
            break

        elif user_2 == 1 and PC == 2:
            i += 1
            print(f'\nVocê ganhou!\nEscolha PC: {PC}')
            print(f'Quantidade de vitórias nº {i}')
            PC = random.randint(1, 2)

        elif user_2 == 2 and PC == 1:
            i += 1
            print(f'\nVocê ganhou!\nEscolha PC: {PC}')
            print(f'Quantidade de vitórias nº {i}')
            PC = random.randint(1, 2)


        elif user_2 == 2 and PC == 2:
            print(f'\nVocê perdeu para a máquina, o resultado foi par.\nEscolha PC: {PC}')
            print(f'Quantidade de vitórias nº {i}')
            break


    if user_1 == 2:
        if user_2 == 1 and PC == 1:
            i += 1
            print(f'\nVocê ganhou!\n Escolha PC: {PC}')
            print(f'Quantidade de vitórias nº {i}')
            PC = random.randint(1, 2)


        elif user_2 == 1 and PC == 2:
            print(f'\nVocê perdeu para a máquina, o resultado foi impar.\nEscolha PC: {PC}')
            print(f'Quantidade de vitórias nº {i}')
            break

        elif user_2 == 2 and PC == 1:
            print(f'\nVocê perdeu para a máquina, o resultado foi impar.\nEscolha PC: {PC}')
            print(f'Quantidade de vitórias nº {i}')
            break

        elif user_2 == 2 and PC == 2:
            i += 1
            print(f'\nVocê ganhou!\n Escolha PC: {PC}')
            print(f'Quantidade de vitórias nº {i}')
            PC = random.randint(1, 2)