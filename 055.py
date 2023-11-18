#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois, deve mostrar para cada palavra, suas vogais

tupla = ('Teclado', 'CPU', 'Monitor', 'Mouse')
'''
for i in range(0, len(tupla)):
    cont_vogais_up = tupla[i].count('a') + tupla[i].count('e') + tupla[i].count('i') + tupla[i].count('o') + tupla[i].count('u')
    cont_vogais_down = tupla[i].count('A') + tupla[i].count('E') + tupla[i].count('I') + tupla[i].count('O') + tupla[i].count('U')
    vogais = cont_vogais_up + cont_vogais_down
    
    print(f'A quantiade de vogais em **{tupla[i]}** é de {vogais}')
'''

for palavra in tupla:
    print(f'\n{palavra}')
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            print(f'{letra}', end = ' ')