""" Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
pessoas = [] # principal
dados = [] # temporário
contagem = 0
maiorpeso = menorpeso = 0
resposta = 'S'
while resposta == 'S':
    nome = str(input('Digite o nome: ')).strip().capitalize()
    dados.append(nome)
    peso = float(input('Digite o peso [kg]: '))
    dados.append(peso)
    if len(pessoas) == 0:
        maiorpeso = menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
    pessoas.append(dados[:])
    dados.clear()
    contagem += 1
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('RESPOSTA INVÁLIDA!\nQuer continuar? [S/N] ')).upper().strip()[0]
print('')
print('-=-' * 25)
print(f'\nForam cadastradas {contagem} pessoas.')
print(f'\n O maior peso foi de {maiorpeso}kg, Peso de ', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'\n O menor peso foi de {menorpeso}kg, Peso de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}] ', end='')
print()
print('\nFIM DO PROGRAMA')