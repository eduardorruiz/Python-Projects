from time import sleep
number = int(input('Digite o número que será verificado: '))
resultado = number % 2
print('Analisando...')
sleep(1.2)
print('-=-' *25)
if resultado == 0:
    print(f'O número {number} é PAR!')
else:
    print(f'O número {number} é ÍMPAR!')
print('-=-'*25)
