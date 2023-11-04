#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
'''
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
'''
resposta = None
quant_entradas = 0
soma = 0
maior = None
menor = None

while resposta != 'N':
    numero = float(input('Digite um número: '))
    quant_entradas += 1
    soma += numero
    resposta = input('Deseja continuar? [S/N]').upper()

    if maior == None and menor == None:
        maior = numero
        menor = numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

media = soma / quant_entradas

print(f'A média é {media}\n'
      f'O maior é {maior}\n'
      f'O menor é {menor}\n')