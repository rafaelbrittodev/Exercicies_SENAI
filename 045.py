#Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000

while True:
      print('***** Gerador de Tabuada *****')
      n = int(input('Digite um número: \n'))

      if n == '0000':
            break

      for i in range(1,11):
            print(f'{n} * {i} = {int(n) * i}')