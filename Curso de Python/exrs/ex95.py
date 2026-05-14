""" Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador."""

from time import sleep
jogador = dict()
time = list()
gols_feitos = list()
total_de_gols = 0
continuar = 'S'
código_do_jogador = 0
while continuar == 'S':
    jogador['código_do_jogador'] = código_do_jogador
    código_do_jogador += 1
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    sleep(0.3)
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    jogador['partidas'] = partidas
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols {jogador["nome"]} marcou na partida {c + 1}: '))
        gols_feitos.append(gols)
        jogador['gols'] = gols_feitos
        total_de_gols += gols
        sleep(0.3)
    jogador['total_de_gols'] = total_de_gols
    time.append(jogador.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Erro, digite apenas S ou N.')
        continuar = str(input('Novamente, quer continuar? [S/N] ')).strip().upper()

    print('-=' * 20)
for jogadores in time:
    print(jogadores)
    print('- ' * 38)
resposta = str(input('Deseja ver dados específicos de algum jogador [S/N]: ')).strip().upper()[0]
while resposta not in 'SN':
    resposta = str(input('Erro, digite apenas S ou N.\nNovamente, deseja ver dados de algum jogador específico [S/N]: ')).strip().upper()
print('- ' * 26)
if resposta == 'S':
    continua = 0
    while continua != 999:
        continua = int(input('Qual é o código do jogador que deseja ver os dados (Digite 999 para parar): '))
        contagem = continua + 1
        print(f'LEVANTAMENTO DE DADOS do jogador {time[continua]['nome']}: ')
        for c in range(0, jogador['partidas']):
            print(f'    --> Na partida {c + 1}, {time[continua]['nome']} fez {gols_feitos[c]} gols.')

# PRECISO DAR UM JEITO DE COLOCAR A QUANTIDADE DE GOLS DO JOGADOR EM CADA PARTIDA
# E Arrumar a lista gols:
"""
for c in range(0, partidas):
    print(f'    --> Na partida {c + 1}, fez {gols_feitos[c]} gols.')
"""