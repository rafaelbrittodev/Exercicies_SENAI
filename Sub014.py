#Calculadora de Gorjeta
#Solicite ao usuário o valor da conta e a porcentagem da gorjeta que eles gostariam de dar, em seguida, calcule o valor total da conta incluindo a gorjeta.

conta = float(input('Digite o valor total da conta em R$: '))
taxa_gorjeta = float(input('Digite a porcentagem (%) de gorjeta desejada: '))

gorjeta = (conta / 100) * taxa_gorjeta
total_conta = gorjeta + conta


print(f'\nO valor da gorjeta foi de R$ {gorjeta:.2f},'
      f'\nO valor total da compra foi de R$ {total_conta:.2f}')