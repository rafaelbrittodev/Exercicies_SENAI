# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

def sub_carac(a):
    a.split()
    fist_carac = a[0]
    ult_carac = a[-1]

    if fist_carac == '(' and ult_carac == ')':
        print(f'A expressão está correta: {a}')
    else:
        print('A expressão está errada.')

exp = input('Digite uma expressão com parênteses: ')
sub_carac(exp)
