#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

n = int(input('Digite um número: '))
continuar = ''
soma = n
contador = 1
menor = n
maior = n

while continuar != "N":
    n = int(input('Digite um número: '))
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()
    contador += 1
    soma = soma + n

    if n < menor:
        menor = n
    elif n > maior:
        maior = n

media = soma / contador
print(f'A média dos valores é de {media}, o menor valor é {menor}, o maior valor é {maior}')

