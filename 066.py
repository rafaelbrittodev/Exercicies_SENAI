# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
# lidos pelo teclado. No final mostre a matriz na tela, com a formatação correta
def matriz3x3():
    matriz = []

    for i in range(3):
        matriz.append([0] * 3)

    print(*matriz[0])
    print(*matriz[1])
    print(*matriz[2])

    for i in range(3):
        valor = int(input('Digite um valor INT: '))
        matriz[0].pop(-1)
        matriz[0].insert(i, valor)
        print(*matriz[0])
        print(*matriz[1])
        print(*matriz[2])

    for i in range(3):
        valor = int(input('Digite um valor INT: '))
        matriz[1].pop(-1)
        matriz[1].insert(i, valor)
        print(*matriz[0])
        print(*matriz[1])
        print(*matriz[2])

    for i in range(3):
        valor = int(input('Digite um valor INT: '))
        matriz[2].pop(-1)
        matriz[2].insert(i, valor)
        print(*matriz[0])
        print(*matriz[1])
        print(*matriz[2])

matriz3x3()

