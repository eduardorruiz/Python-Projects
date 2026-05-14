""" Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador."""
jogador = dict()
time = list()
gols_feitos = list()
continuar = 'S'
código_do_jogador = 0
while continuar == 'S':
    jogador['código_do_jogador'] = código_do_jogador
    código_do_jogador += 1
    jogador['nome'] = str(input('Nome do jogador: ')).capitalize().strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    gols_feitos.clear()
    jogador['partidas'] = partidas
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols {jogador["nome"]} marcou na partida {c + 1}: '))
        gols_feitos.append(gols)
    jogador['gols'] = gols_feitos[:]
    jogador['total_de_gols'] = sum(gols_feitos)
    time.append(jogador.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Erro, digite apenas S ou N.')
        continuar = str(input('Novamente, quer continuar? [S/N] ')).strip().upper()
# MOSTRAR O RESULTADO
    print('-=' * 20)
for jogadores in time:
    print(jogadores)
    print('- ' * 38)
resposta = str(input('Deseja ver dados específicos de algum jogador [S/N]: ')).strip().upper()[0]
while resposta not in 'SN':
    resposta = str(input('Erro, digite apenas S ou N.\nNovamente, deseja ver dados de algum jogador específico [S/N]: ')).strip().upper()
print('- ' * 26)
while resposta == 'S':
    cod = int(input('Qual é o código do jogador que deseja ver os dados: '))
    print(f'LEVANTAMENTO DE DADOS do jogador {time[cod]['nome']}: ')
    for c in range(0, len(time[cod]['gols'])):
        print(f'    --> Na partida {c + 1}, {time[cod]['nome']} fez {time[cod]['gols'][c]} gols.')
    resposta = str(input('Deseja ver dados específicos de mais algum jogador [S/N]: ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Erro, digite apenas S ou N.\nNovamente, deseja ver dados de algum jogador específico [S/N]: ')).strip().upper()
    print('- ' * 26)
print('\n- Fim do Programa -')