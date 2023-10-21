#Calculadora de Juros Compostos
#Solicite ao usuário o principal, a taxa de juros anual e o número de anos, e imprima o valor do investimento após esse número de anos

valor_investimento = float(input('Digite o valor do investimento desejado em R$: '))
juros_anual = float(input('Informe a taxa de juros anual: '))
anos = int(input('Digite quantos anos o dinheiro ficará investido: '))

resultado_total = valor_investimento + (juros_anual * anos)
rentabilidade = resultado_total - valor_investimento
juros_acumulado = juros_anual * anos

print(f'\nInvestimento inicial R$ {valor_investimento:.2f}\nRentabilidade: {juros_acumulado:.2f}%\nTempo investido: {anos} anos\nTaxa de juros anual: {juros_anual:.2f}%, '
      f'\nRentabilidade Total R$ {rentabilidade:.2f}\nValor total a ser resgatado R$ {resultado_total:.2f}')