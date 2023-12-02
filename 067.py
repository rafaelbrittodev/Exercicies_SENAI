# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta
import random

matriz = []
n = int(input('Quantos jogos deseja gerar: '))

for i in range(n):
    matriz.append([0] * 6)

for i in range(0, n):
    for x in range(0, 6):
        valor = random.randint(1,60)
        if valor not in matriz[i]:
            matriz[i].pop(-1)
            matriz[i].insert(x, valor)
            

for i in range(0, n):

    print(f'Jogo nº{i+1}\n{matriz[i]}\n')


