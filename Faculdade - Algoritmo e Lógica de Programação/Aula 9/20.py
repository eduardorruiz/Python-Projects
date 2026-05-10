"""Faça um programa que leia um número inteiro N obrigatoriamente maior que 10. Preencha uma lista de tamanho
N com números inteiros aleatórios. Exiba na tela a lista gerada e em seguida coloque-a em ordem crescente
usando o método da bolha. Não é permitido usar o método sort da lista"""
from random import randint
lista = []
N = int(input('Digite o valor de N: '))
while N < 11:
    print('Erro, porfavor insira um valor maior que 10')
    N = int(input('Digite o seu novo valor de N: '))
for c in range(1, N):
    num = randint(1, 100)
    lista.append(num)
print(lista)