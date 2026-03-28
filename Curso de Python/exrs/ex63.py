print('-*-' * 10)
print('Sequência de Fibonacci')
print('-*-' * 10)
n = int(input('\nQuantos termos da sequência de Fibonacci você quer ver: '))
if n != 0:
    t1 = 0
    cont = 3
    t2 = 1
    print('~~' * 30)
    print(f'{t1} --> {t2}', end='')
    while cont <= n:
        t3 = t1 + t2
        print(f' --> {t3}', end='')
        t1 = t2
        t2 = t3
        cont += 1
    print('')
    print('~~' * 30)
print('\nFim do Programa')
