#Crie um programa que pede ao usuário para digitar dois números e, em seguida,
#divide o primeiro número pelo segundo número. No entanto, o programa deve ser capaz de lidar com a
#possibilidade de o usuário digitar um valor inválido, como uma string ou o número zero.
#
#ZeroDivisionError ; ValueError

while True:
    try:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o denominador da divisão: '))
        resultado = n1 / n2
        print(f'\n{n1} / {n2} = {resultado}')

    except ZeroDivisionError:
        print('Não é possível dividir por zero. Tente novamente.')

    except ValueError:
        print('Valor inválido. Tente novamente.')