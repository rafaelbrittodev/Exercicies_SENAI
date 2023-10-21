#Calculadora de IMC
#Solicite ao usuário sua altura e peso, e calcule seu Índice de Massa Corporal (IMC).

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

IMC = peso / (altura * altura)

print(f'Seu IMC é de {IMC:.2f}')