"""Crie um programa que vai ler vários números e colocar em uma lista
Depois disso, mostre
A) Quantos números foram digitados
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista."""
lista = []
inversa = []
contador = 1
n = int(input('Digite um valor: '))
lista.append(n)
stop = str(input('Deseja continuar? [S/N] ')).strip().upper()
while stop != 'S' and stop != 'N':
    stop = str(input('Deseja continuar? [S/N] ')).strip().upper()
while stop == 'S':
    n = int(input('Digite um valor: '))
    stop = str(input('Deseja continuar? [S/N] ')).strip().upper()
    lista.append(n)
    contador += 1
if contador > 1:
    print(f'Foram adicionados {contador} valores na lista.')
else:
    print(f'Foi adicionado 1 valor na lista.')
print(lista)
lista.sort(reverse=True)
print(f'A lista de valores, em ordem decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado na lista.')
else:
    print('O valor 5, não está na lista.')
