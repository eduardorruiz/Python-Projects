"""Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50) e em seguida preencha uma lista
com N elementos inteiros gerados aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random –
veja o quadro sobre isso no exercício 9)."""
from random import randint
N = int(input('Digite N: '))
cont = 0
lista = []
while N <= 0 or N >= 50:
    print('valor invalido')
    N = int(input('Digite N novamente: '))
while cont < N:
    n = randint(0, 1000)
    lista.append(n)
    cont += 1
print(lista)