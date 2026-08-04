""" Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
mostrar a soma entre todos os valores pares sorteados pela função anterior."""

from random import randint
numeros = list()
def sorteia():
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print('Sorteando 5 valores: ', end='')
    print(numeros)
def somapar():
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {numeros}, temos {soma}. ')
sorteia()
somapar()