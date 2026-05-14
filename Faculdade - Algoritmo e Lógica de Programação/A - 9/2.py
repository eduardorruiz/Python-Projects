""" Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela na ordem
inversa à ordem de leitura, sendo um elemento por linha da tela. """

lista = []
cont = 0
i = 1
while cont < 10:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
print(lista)
while i < 11:
    print(lista[10 - i])
    i += 1