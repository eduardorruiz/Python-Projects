print('{:-^50}'.format(' ANALISADOR DE PRIMOS '))
num = int(input('Digite o numéro a ser analisado: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[m', end='')
    print(c, end=' - ')
print('\033[mAcabou.')
print(f'O número {num} foi dividido {total} vezes.')
if total == 2:
    print('Por isso ele é \033[1mPRIMO\033[m.')
else:
    print('Portanto, ele \033[1mNÃO é PRIMO\033[m.')
