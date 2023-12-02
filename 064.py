# Crie um programa onde o usuário possa digitar sete letras,
# e cadastre em uma única lista, que mantenha separado as consoantes das vogais

list = [[],[]]


for i in range(1,8):
    i = str(input(f'Digite a {i}º letra: '))

    if i in 'aeiouAEIOU':
        list[0].append(i)
    else:
        list[1].append(i)

print(f'As vogais são {list[0]}'
      f'\nE as consoanges são {list[1]}'
      f'\nA lista completa é {list}')



