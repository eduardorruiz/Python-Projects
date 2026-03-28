""" Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

saque = int(input('Digite o valor do saque: R$'))
ncinquenta = nvinte = ndez = num = 0
if saque >= 50:
    while saque >= 50:
        saque -= 50
        ncinquenta += 1
        while 50 > saque >= 20:
            saque -= 20
            nvinte +=1
            while 20 > saque >= 10:
                saque -= 10
                ndez += 1
                while 10 > saque >= 1:
                    saque -= 1
                    num += 1
if 50 > saque >= 20:
    while 50 > saque >= 20:
        saque -= 20
        nvinte += 1
        while 20 > saque >= 10:
            saque -= 10
            ndez += 1
            while 10 > saque >= 1:
                saque -= 1
                num += 1
if 20 > saque >= 10:
            while 20 > saque >= 10:
                saque -= 10
                ndez += 1
                while 10 > saque >= 1:
                    saque -= 1
                    num += 1
if 10 > saque >= 1:
        while 10 > saque >= 1:
            saque -= 1
            num += 1
if ncinquenta > 0:
    print(f'Total de {ncinquenta} cédulas de R$50')
if nvinte > 0:
    print(f'Total de {nvinte} cédulas de R$20')
if ndez > 0:
    print(f'Total de {ndez} cédulas de R$10')
if num > 0:
    print(f'Total de {num} cédulas de R$1')
