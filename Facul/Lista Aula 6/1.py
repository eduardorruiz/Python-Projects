''' Escreva um programa que leia um número inteiro e em seguida apresente na tela a tabuada de 0 a 10
para esse número fornecido. '''
print('Tabuada')
num = int(input('Digite um numero inteiro: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
print('\nFim do programa')