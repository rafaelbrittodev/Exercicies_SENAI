#Escreva um programa que leia uma frase,
#e mostre uma formatação adaptável de acordo com o tamanho da frase, coordenado por uma função
#
#Exemplo:
#       ----------------------------
#            Senai Show de bola
#       ----------------------------

def format(msg):
    print('---' * 10)
    print(msg)
    print('---' * 10)

a = 'Senai Show de bola'
format(f'{a.center(30)}')