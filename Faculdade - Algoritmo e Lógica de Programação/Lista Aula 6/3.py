""" Escreva um programa que leia um número inteiro N e em seguida leia N números reais, separando o
menor e o maior, apresentando-os na tela."""

nint = int(input('Digite um número inteiro: '))
nreal = float(input('Digite um número real: '))
parar = str(input('Deseja continuar [s/n]: ')).lower()
print('-' * 25)
maiorreal = nreal
menorreal = nreal
while parar != 'n':
    if nreal > maiorreal:
        maior = nreal
    if nreal < menorreal:
        menor = nreal
    nreal = float(input('Digite mais um número real: '))
    parar = str(input('Deseja continuar [s/n]: ')).lower()
    print('-' * 25)
if nint > maiorreal:
    maior = nint
if nint < maiorreal:
    maior = maiorreal
if nint < menorreal:
    menor = nint
if nint > menorreal:
    menor = menorreal
print(f'\nO maior número informado foi [{maior}] e o menor foi [{menor}].')