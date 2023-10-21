#Jogo da Adivinhação
#Escolha um número aleatório entre 1 e 10, depois peça ao usuário para adivinhar o número.
import random

a = random.randint(1, 10)

escolha = int(input('Tente adivinha o número da máquina de 0 até 10.\nDigite seu número: '))

if escolha == a:
    print(f'\nParabéns, você acertou! A máquina escolheu {a}!!!')
else:
    print(f'\nNão foi dessa vez, a máquina escolheu {a}...')