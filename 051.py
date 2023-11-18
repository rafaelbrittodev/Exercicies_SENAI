#Escreva um programa que tenha uma função, verifica_par(), que receba um número e verifique se é par


def verifica_par():
    n = int(input('Digite um número: '))

    if n % 2 == 0:
        print(f'O número digitado é PAR.')
    else:
        print(f'O número digitado é IMPAR')

try:
    while True:
        verifica_par()

except ValueError:
        print('Valor inválido. Tente novamente.')


