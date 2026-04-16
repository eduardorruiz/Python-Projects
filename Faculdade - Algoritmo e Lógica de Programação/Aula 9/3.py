"""Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50) e em seguida leia N números reais
em uma lista A. Exiba a lista na tela, um elemento por linha."""
N = int(input('Digite N: '))
cont = 0
lista = []
while N <= 0 or N >= 50:
    print('valor invalido')
    N = int(input('Digite N novamente: '))
while cont < N:
    n = int(input('Digite N: '))
    lista.append(n)
    cont += 1
for valor in lista:
    print(valor)