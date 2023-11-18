#Escreva um programa que leia uma frase,
#e mostre uma formatação adaptável de acordo com o tamanho da frase, coordenado por uma função
#
#Exemplo:
#       ----------------------------
#            Senai Show de bola
#       ----------------------------

def titulo(frase, arg = '*'):
    print(arg * 2 * len(a))
    print(f'{a.center(len(a) * 2)}')
    print(arg * 2 * len(a))



a = input('Digite uma frase: ')
titulo(a, arg = '-')

