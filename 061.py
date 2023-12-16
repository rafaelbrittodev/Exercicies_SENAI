'''Escreva um programa que crie uma lista vazia e permita que o usuário insira números nessa lista até que ele
digite um número negativo. Em seguida, exiba a lista na tela.'''

while True:
    try:
        lista=[]

        while True:
            numeros= int(input("Digite um número: "))
            if numeros < 0:
                break
            else:
                lista.append(numeros)

        print(f'Lista completa: {lista}')
        break
    except ValueError:
        print('Só aceitamos números inteiros!')