#Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:
#1 Apenas os 3 primeiros mais assistidos
#2 Os últimos 2 mais assistidos
#3 A lista em ordem alfabética
#4 Em que posição está “O rei leão”

filmes_mais_assistidos = ('Avatar', 'Vingadores: Ultimado', 'Avatar: O caminho da água', 'Titanic', 'Star Wars: O Despertar da Força',
                          'Vingadores: Guerra Infinita', 'Homem-Aranha: Sem volta para casa', 'Jurassic World', 'O Rei Leão', 'Os Vingadores')


print('\nTOP 3 FILMES MAIS ASSISTIDOS:')
for i in range(0, 3):
    print(filmes_mais_assistidos[i])

print('\n2 ULTIMOS FILMES MAIS ASSISTIDOS DO TOP 10')
for i in range(1, 3):
    print(filmes_mais_assistidos[-i])

print('\n TOP 10 FILMES MAIS ASSISTIDOS EM ORDEM ALFABÉTICA')
print(f'{sorted(filmes_mais_assistidos)}')

print('\nPOSIÇÃO DO REI LEÃO NO TOP 10')
print(f'{filmes_mais_assistidos.index('O Rei Leão')}º Lugar')
