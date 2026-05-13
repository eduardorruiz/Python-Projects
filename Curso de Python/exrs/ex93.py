""" Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""
from time import sleep
gols_feitos = list()
jogador = dict()
total_de_gols = 0
jogador['nome'] = str(input('Nome do jogador: '))
sleep(0.3)
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(0, partidas):
    gols = int(input(f'Quantos gols {jogador["nome"]} marcou na partida {c + 1}: '))
    gols_feitos.append(gols)
    jogador['gols'] = gols_feitos
    total_de_gols += gols
    sleep(0.3)
jogador['total_de_gols'] = total_de_gols
sleep(1)
print('-='*20)
print(jogador)
print('-='*20)
sleep(1)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*20)
sleep(1)
print(f'O {jogador["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'    --> Na partida {c + 1}, fez {gols_feitos[c]} gols.')

