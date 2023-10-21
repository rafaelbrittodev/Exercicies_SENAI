#Gerador de Histórias
#Solicite ao usuário seu nome, sua cidade e seu animal de estimação, então use essas informações para gerar uma história curta.
import random

nome = input('Digite o seu nome: ')
cidade = input('Digite o nome de sua cidade: ')
animal = input('Digite o nome de seu animal de estimação: ')

frase_1 = ['Era uma vez ','No sabádo passado, ','Hoje, ' ]
frase_2 = [' que estava triste, decidiu sair para a cidade de ', ' que estava feliz decidiu voltar para a cidade de ', ' que estava tão zangado que foi para a cidade de ']
frase_3 = [', mas chegando lá ficou surpreso por encontrar nas ruas seu pet ', ' mas chegando lá notou que esqueceu em casa seu pet ', ' e ao seu lado estava seu fiel companheiro pet ']


print(frase_1[random.randint(0,2)] + nome + frase_2[random.randint(0,2)] + cidade + frase_3[random.randint(0,2)] + animal)

