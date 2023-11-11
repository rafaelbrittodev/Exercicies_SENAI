#Crie um programa para jogar par ou ímpar com o usuário,
#e só pare quando perder. Ao final deve mostrar a quantidade de vitórias

import random
'''
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
'''

vitorias = 0

while True:
    jogador = int(input('Digite sua jogada: \n'))
    jogador_escolha = input('Escolha Par ou Impar [P/I]: \n')
    Pc = random.randint(1,10)
    soma = jogador + Pc

    if soma % 2 == 0 and jogador_escolha == 'P':
        vitorias += 1
        print(f'Você ganhou, eu joguei {Pc}, e a soma deu {soma}.')

    elif soma % 2 != 0 and jogador_escolha == 'I':
        print(f'Você ganhou, eu joguei {Pc}, e a soma deu {soma}.')

    else:
        print(f'Você perdeu, eu joguei {Pc}, e a soma deu {soma}.')
        break

print(f'Você ganhou {vitorias} vezes, até a próxima!')