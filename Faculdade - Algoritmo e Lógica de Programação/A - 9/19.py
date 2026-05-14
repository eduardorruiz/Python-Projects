"""Faça um programa que permaneça em laço até que seja digitado um valor menor ou igual a zero. Cada valor válido
(positivo) digitado deve ser inserido em uma lista na posição imediatamente antes do primeiro elemento que seja
maior que valor que está sendo inserido. Isso resultará em uma lista ordenada de forma crescente. Será
necessário usar o método insert da lista – pesquise sobre ele."""
lista = []
print('Para parar, digite um valor menor ou igual a 0.')
num = int(input('Digite o valor de N: '))
lista.append(num)
while num > 0:
    num = int(input('Digite o valor de N: '))
# FALTA TERMINAR