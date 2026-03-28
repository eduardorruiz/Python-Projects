'''Escreva um programa que contenha um laço que será executado enquanto o número digitado for
diferente de zero. Para cada número digitado pelo usuário mostrar na tela apenas os que forem divisíveis
por 2 e por 3.'''
num = int(input('Digite um número: '))
while num != 0:
    if num % 2 == 0 and num % 3 == 0:
        print(num)
    num = int(input('Digite um número: '))
print('\nFim do Programa')