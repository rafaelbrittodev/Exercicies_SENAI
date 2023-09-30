#O comando print retorna informações para o usuário
#print("Olá, meu nome é Rafael Brito")
'''
idade = 24
print(f'Minha idade é {idade}')

#Escreva um programa que leia a idade do usuário e retorne sua idade
idade = input("Digite a sua idade: ")
print(f'Sua idade é {idade}')

#Modo antigo de formatar um print, versão python 2
print('Sua idade é ',idade)

N1 = int(input('Digite o primeiro número: '))
N2 = int(input('Digite o segundo número: '))

Soma = N1 + N2

print(f'A soma de N1 e N2 é {Soma}')

Nome = 'Rafael'
Sobrenome = 'Brito'
Nome_completo = Nome + ' ' + Sobrenome
print(Nome_completo)
'''
'''
#Declaração de variável
Nome = input('Digite seu nome: ')

Nome = Nome.strip() #Remove os espaços a direita e esquerda
print(f'A primeira letrata é: {Nome[0]}') Analiso a primeira letra da STRING

print(f'O tamanho do seu nome é {len(Nome)}') #A Função len(), retorna o tamanho da STRING

Nome = Nome.split() #Separa nossa STRING em lista
print(f'O Primeiro nome é: {Nome[0]}') #Analisando o Primeiro Nome
''''''
Nome = ['Rafael', 'da', 'Silva', 'Brito']
Nome = '/'.join(Nome) #O método .join junta elementos da minha STRING
print(Nome)

Nome = input('Digite o seu nome: ')
Nome = Nome.upper() #Transforma toda minha STRING em Maiusculo
print(Nome)
Nome = Nome.lower() #Transforma toda minha STRING em Minusculo
print(Nome)'''
'''
altura = float(input('Digite sua altura: '))
if altura > 1.5: #Comparação de variável
    print('Você pode andar no brinquedo!')
else:   # Saída negativa
    print('Quem sabe no ano próximo ano!')
    
#--------------------------------------------
if altura > 1.5 and altura < 2:
    print('Você pode andar no Brinquedo.')
elif altura > 2:
    print('Você irá bater a cabeça! Está proibido!')
else:
    print('Você é muito pequeno, quem sabe no próximo ano.')
'''
