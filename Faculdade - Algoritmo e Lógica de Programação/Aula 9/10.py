""" Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random). Exiba na tela a lista gerada. Em
seguida, o programa deve ler um valor X e informar se tal valor está, ou não está presente, bem como informar a
posição de X na lista. Se houver mais de uma ocorrência de X na lista informe todas as posições. Neste exercício
não é permitido usar os operadores in e not in. Também não é permitido usar qualquer função pronta de Python"""
from random import randint
N = int(input('Digite N: '))
cont = i = 0
lista = []
while cont < N:
    n = randint(0, 1000)
    lista.append(n)
    cont += 1
print(lista)
X = int(input('Digite X: '))
while i < N:
    if lista[i] == X:
        print(f'{X} foi encontrado na lista, como elemento [{i}]')
    i += 1
if X not in lista:
    print(f'{X} não está na lista.')
