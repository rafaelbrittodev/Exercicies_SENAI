#Crie um programa que verifica se uma pessoa pode ser doadora de sangue,
#considerando a idade e os critérios de saúde.

def check_idade(a):
    if a >= 16:
        print('Você tem idade suficiente para ser doador de sangue.')
    else:
        print('Você não tem idade suficiente para ser doador de sangue')

def check_saude(a):
    while True:
        if a == 1:
            print('Você está em condições saudáveis para realizar sua doação!')
            break
        elif a == 2:
            print('Você não está com condições de saúde para realizar sua doação.')
            break
        else:
            print('Opção inválida. Por favor digite 1 ou 2.')
            a = int(input('Digite [1] se você está em condições saudáveis ou [2] caso esteja doente: '))

idade = int(input('Digite sua idade: '))
check_idade(idade)

if idade >= 16:
    saude = int(input('Digite [1] se você está em condições saudáveis ou [2] caso esteja doente: '))
    check_saude(saude)

