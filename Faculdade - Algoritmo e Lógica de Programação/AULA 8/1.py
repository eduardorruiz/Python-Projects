""" Escreva um programa que permaneça em laço até que seja digitado o valor zero ou negativo. Cada valor
positivo lido deve ser inserido no final de uma lista, usando o método append. Ao final exiba a lista
completa na tela. """
num = int(input('Digite o primeiro valor: '))
lista = []
if num > 0:
    lista.append(num)
while num > 0:
    num = int(input('Digite um valor: '))
    if num > 0:
        lista.append(num)
print(lista)