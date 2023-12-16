#Escreva um programa que crie uma lista com os números de 1 a 10 e, em seguida, exiba apenas os números ímpares da lista.

numeros=[1,2,3,4,5,6,7,8,9,10]
impares=[]

for impar in numeros:
    if impar % 2 != 0:
        impares.append(impar)
print(f'Números ímpares: {impares}')