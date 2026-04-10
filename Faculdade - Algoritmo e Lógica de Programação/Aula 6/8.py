''' Desenvolva um programa que leia do teclado um número inteiro e mostre na tela se esse número é
primo ou não. Lembrando: um número primo é divisível somente por 1 e por ele mesmo. '''
print('-=-' * 12)
print('Verificador de primos')
print('-=-' * 12)
n = int(input('Digite um número: '))
cont = 1
total = 0
while cont <= n:
    if n % cont == 0:
        total += 1
    cont += 1
if total == 2:
    print(f'\nO número [{n}] é primo!')
else:
    print(f'\nO número [{n}] não é primo!')
print('\nFim do Programa')
