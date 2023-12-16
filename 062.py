'''Escreva um programa que crie duas listas com 5 números cada uma e exiba a soma dos elementos correspondentes
das duas listas. Por exemplo, se as listas forem [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1], o programa deve exibir [6, 6, 6, 6, 6].
'''
import random


cont=0
lista_1=[]
lista_2=[]
lista_soma=[]

while cont<5:
    numero_1=random.randint(1,10)
    numero_2 = random.randint(1, 10)
    lista_1.append(numero_1)
    lista_2.append(numero_2)
    cont+=1

for elemento in range(0,5):
    lista_soma.append(lista_1[elemento] + lista_2[elemento])

print(lista_1)
print(lista_2)
print(lista_soma)