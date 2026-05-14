"""Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random). Exiba na tela a lista gerada. Em
seguida, o programa deve ler um valor X e informar se tal valor está, ou não está presente na lista. Neste exercício
é permitido usar os operadores in e/ou not in. """
from random import randint
N = int(input('Digite N: '))
cont = 0
lista = []
while cont < N:
    n = randint(0, 1000)
    lista.append(n)
    cont += 1
print(lista)
X = int(input('Digite X: '))
if X in lista:
    print(f'{X} está na lista')
else:
    print(f'{X} não está na lista')