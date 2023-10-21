#Impressora de Nomes
#Solicite o nome do usuário e imprima cada letra do nome em uma nova linha.

nome = input('Digite seu nome: ')

qt_letras = len(nome)

for i in range(0, qt_letras):
    print(nome[i])
