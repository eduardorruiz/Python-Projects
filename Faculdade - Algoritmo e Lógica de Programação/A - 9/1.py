"""Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela um elemento
por linha."""
list = []
for c in range(1, 11):
    n = int(input('Digite um valor: '))
    list.append(n)
for valor in list:
    print(valor)