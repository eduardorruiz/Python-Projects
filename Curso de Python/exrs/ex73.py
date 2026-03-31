""" Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.    b) Os últimos 4 colocados.
c) Times em ordem alfabética.    d) Em que posição está o time da Corinthians."""


print('- - - - - - -Lista de times do Brasileirão 2025- - - - - - - -')
brasileirão = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo',
               'Bahia', 'São Paulo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Santos',
               'Corinthians', 'Vasco da Gama', 'Vitória', 'Internacional','Ceará',
               'Fortaleza', 'Juventude', 'Sport Recife')
print(f'Lista de times do Brasileirão: {brasileirão}')
# for times in brasileirão: mostraria em lista uma em baixo da outra.
print('-*-' * 29)
quinto = brasileirão[:5]
print(f'Os 5 primeiros colocados são: {quinto}')
print('-*-' * 29)
ultimos = brasileirão[-4:] #poderia colocar também [16:]
print(f'Os últimos 4 times são {ultimos}')
print('-*-' * 29)
ordem = sorted(brasileirão)
print(f'Os times em ordem alfabetica são: {ordem}')
print('-*-' * 29)
corinthians = brasileirão.index('Corinthians') + 1
print(f'O Corinthians está na {corinthians}° posição')