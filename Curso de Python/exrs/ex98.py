""" Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em | b) de 10 até 0, de 2 em 2 | c) uma contagem personalizada"""
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-*-' * 15)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    else:
        for c in range(i, f-1, p * (-1)):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')

# PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 15)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('De quanto em quanto: '))
contador(ini, fim, pas)