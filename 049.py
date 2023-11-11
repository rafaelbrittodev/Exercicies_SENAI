#Crie um programa que tenha a função área(),
#que receba as dimensões de um muro retangular e mostra a área do terreno

def calc_area(a,b):
    area = a * b
    return area

while True:
    try:
        print(f'***** Calculadora de Área *****')
        a = float(input('Digite a altura: \n'))
        b = float(input('Digite a largura: \n'))

        area = calc_area(a,b)

        print(f'A área é {area:.2f}m²')
        break
    except:
        print('\nErro não identificado. Tente novamente.\n')
