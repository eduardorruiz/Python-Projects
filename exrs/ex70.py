"""Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""
total = totalmil = cont = menor = maior = 0
barato = caro = ' '

while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: R$'))
    total += preco
    cont += 1
    if cont == 1 or preco < menor: #simplificado
        menor = preco
        barato = produto
#    else:
#        if preco < menor:
#            menor = preco
#            barato = produto
    if cont == 1: #extenso
        maior = preco
        caro = produto
    else:
        if preco > menor:
            maior = preco
            caro = produto
    if preco > 1000:
        totalmil += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto na compra foi de R${total}')
print(f'Temos {totalmil} produtos custam mais de R$1000')
print(f'O produto mais barato foi [{barato}] que custa R${menor}')
print(f'E o produto mais caro foi [{caro}] que custa R${maior}')