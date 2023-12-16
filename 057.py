# Faça um programa com uma função maior e menor, que leia uma lista com 5 valores informados
# pelo usuário e retorne esses valores e a posição deles


def maior(lista):
    return max(lista)
def menor (lista):
    return min (lista)

while True:
    try:
        cont=0
        lista=[]

        while cont<5:
            numero=int(input("Digite um número: "))
            cont+=1
            lista.append(numero)

        print(f'Maior Número: {maior(lista)}, e está na {lista.index(max(lista))+1}º posição')
        print(f'Menor Número: {menor(lista)}, e está na {lista.index(min(lista))+1}º posição')
        break

    except ValueError:
        print("Só aceitamos números!")