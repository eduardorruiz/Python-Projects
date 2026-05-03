""" Faça um programa que ajude um jogador da MEGASENA a criar palpites.O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import randint
lista = []
palpites = []
cont = 0
print('--' * 22)
print('    PALPITADOR DE JOGOS DA MEGA-SENA!!')
print('--' * 22)
quantidade = int(input('Digite quantos palpites, você deseja gerar: '))
for c in range(0, quantidade):
    cont = 0
    while cont < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
    lista.sort()
    palpites.append(lista[:])
    lista.clear()
enumerador = 1
for palpite in palpites:
    print(f'O {enumerador}ª palpite: {palpite}')
    enumerador += 1
