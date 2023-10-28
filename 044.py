#Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder. Ao final deve mostrar a quantidade de vitórias
import random

PC = random.randint(1,2)

print(f'***** Game par ou impar *****\n')

user_1 = int(input(f'Faça sua escolha:\n'
                   f'[1] para impar.\n'
                   f'[2] para par.'))

user_2 = int(input(f'Escolha:\n'
                   f'[1] Um.\n'
                   f'[2] Dois.'))
'''     
CONTINUAR *************************************************************     
if user == 1 and PC == 1:
    print(f'Você perdeu para a máquina.')
elif user == 1 and PC == 2:
    print(f'Parábens você ganhou da máquina.')
elif user == 1 and PC == 2:
    print(f'Parábens você ganhou da máquina.')
'''