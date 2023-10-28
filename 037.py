#Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo
#até que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.
import random


x = random.randint(1,10)
tentativas = 0
resposta = ''

while resposta != x:
    resposta = int(input('\nDigite um número entre 1 - 10: '))
    tentativas += 1

    print(f'Não foi dessa vez, tente novamente.\n'
          f'O número de tentativas é {tentativas}')



print(f'\nParabéns! Você acertou após {tentativas} tentativas. O número correto é {x}.')