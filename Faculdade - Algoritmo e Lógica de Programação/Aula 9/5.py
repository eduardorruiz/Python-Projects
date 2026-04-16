"""Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50 – o programa deve garantir isso em
um laço) e em seguida leia N números reais em uma lista A. O programa deve separar os valores lidos em A em
outras duas listas NEG e POS, a primeira contendo somente os valores negativos e a segunda contendo os valores
positivos e zero. Apresentar na tela as listas NEG e POS e a quantidade de valores contidos em cada uma."""
A = []
neg = []
pos = []
i = 0
quantidadevaloresneg = quantidadevalorespos = 0
n = int(input('Digite um número: '))
while n <= 0 or n > 50:
    print('Valor invalido')
    n = int(input('Digite um número novamente: '))
while i < n:
    valores = int(input(f'Digite o elemento [{i}] da lista A: '))
    A.append(valores)
    if valores < 0:
        neg.append(valores)
        quantidadevaloresneg += 1
    else:
        pos.append(valores)
        quantidadevalorespos += 1
    i += 1
print(f'A lista A é {A}')
print(f'A lista dos números negativos digitados é {neg} e foram digitados {quantidadevaloresneg} valores.')
print(f'A lista dos números positivos digitados é {pos} e foram digitados {quantidadevalorespos} valores.')