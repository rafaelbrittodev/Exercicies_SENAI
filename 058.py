'''Crie um programa onde serão informados diversos valores em uma lista. Caso o número já exista ele não será
adicionado. No final, serão exibidos todos os valores únicos em ordem crescente'''

while True:
    try:
        valores=[]

        while True:
            numero=int(input("Digite um número ou 0 para parar: "))
            if numero == 0:
                break
            else:
                if numero not in valores:
                    valores.append(numero)
                else:
                    print("Já tem!")

        print(f'Números em ordem crescente: {sorted(valores)}')
        break

    except ValueError:
        print("Só aceitamos números inteiros!")