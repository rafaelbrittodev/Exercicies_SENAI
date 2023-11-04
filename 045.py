#Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000

print('***** Gerador de Tabuada *****')
n = int(input('Digite um número: \n'))

r1 = n * 1
r2 = n * 2
r3 = n * 3
r4 = n * 4
r5 = n * 5
r6 = n * 6
r7 = n * 7
r8 = n * 8
r9 = n * 9
r10 = n * 10

print(f'\nTabuada do {n}:\n'
      f' 1 * {n} = {r1}\n'
      f' 2 * {n} = {r2}\n'
      f' 3 * {n} = {r3}\n'
      f' 4 * {n} = {r4}\n'
      f' 5 * {n} = {r5}\n'
      f' 6 * {n} = {r6}\n'
      f' 7 * {n} = {r7}\n'
      f' 8 * {n} = {r8}\n'
      f' 9 * {n} = {r9}\n'
      f'10 * {n} = {r10}\n')