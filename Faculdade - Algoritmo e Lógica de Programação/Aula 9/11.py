"""Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
aleatoriamente entre 0 e 1000. Exiba na tela a lista gerada. Em seguida, o programa deve ler um valor X e, caso X
esteja na lista, deve eliminá-lo. Caso haja várias ocorrências de X, todas devem ser eliminadas. Pesquise como
usar a função del (você vai precisar dela e neste exercício será permitido usá-la)."""
from random import randint
N = int(input('Digite N: '))
cont = i = 0
lista = []
while cont < N:
    n = randint(0, 10)
    lista.append(n)
    cont += 1
print(lista)
X = int(input('Digite X: '))
if X not in lista:
    print(f'{X} não está na lista.')
while i < N:
    if lista[i] == X:
        print(f'{X} foi encontrado na lista, como elemento [{i}]')
        del lista[i]
        lista.insert(i, 'X') #APENAS ELIMINANDO ESTAVA DANDO ERRO, ENTÃO INSERI UM X ONDE FOI ELIMINADO
    i += 1
print(lista)