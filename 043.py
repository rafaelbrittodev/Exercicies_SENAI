#Crie um programa que leia vários números inteiros.
#O programa só vai parar quando o usuário digitar 0000.
#No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)

soma = 0
i = 0

print(f'********************* Calculator 2K23 **********************\n'
      f'O programa finalizará quando o usuário informar o código 0000')

while True:
    N = input('\nInforme o número desejado: \n')

    if N != '0000':
        N = int(N)
        i += 1
        soma = soma + N

    else:
        print(f'\nQuantidade de números informados: {i}\nA soma total dos números é {soma}')
        break