""" Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e
exiba-a na tela na ordem inversa à ordem de leitura. """

cont = 1
lista = []
for c in range(0, 10):
    num = int(input(f'Digite o {cont}° valor da primeira lista: '))
    lista.append(num)
    cont += 1
lista.reverse()
print(lista)