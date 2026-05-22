""" Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior. """

def maior(* valores):
    cont = maior = 0
    print('-*'*26)
    print('Analisando os valores passados...')
    for num in valores:
        print(f'{num}', end=' ')
        if cont == 0:
            maior = num
        else:
            if num > maior:
                maior = num
        cont += 1
    print(f'--> Foram informados {cont} valores e o maior valor foi [{maior}].')

# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(10, 25, 2, 8, 19, 77)
