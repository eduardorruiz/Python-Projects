""" Escreva um programa que leia um número inteiro N e em seguida leia N números reais,
separando o menor e o maior, apresentando-os na tela. """

n = int(input('N: '))
cont = menor = maior = 0 #se os números fossem negativos daria errado
while cont < n:
    x = float(input(f'Digite o elemento {cont + 1}: '))
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    cont += 1

print(f'O maior valor é {maior}')

