#Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).

def dia_semana(a):
    while True:
        if a == 1:
            print('1 é segunda-feira')
            break
        elif a == 2:
            print('2 é terça-feira')
            break
        elif a == 3:
            print('3 é quarta-feira')
            break
        elif a == 4:
            print('4 é quinta-feira')
            break
        elif a == 5:
            print('5 é sexta-feira')
            break
        elif a == 6:
            print('6 é sábado')
            break
        elif a == 7:
            print('7 é domingo')
            break
        else:
            a = int(input('Opção inválida. Por favor digite um número de 1 até 7: '))
    
dia = int(input('Digite um número de 1 a 7: '))
dia_semana(dia)