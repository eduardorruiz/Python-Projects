''' Escreva um programa que leia um número inteiro N e em seguida apresente na tela os N primeiros
termos da sequência de Fibonacci. Essa sequência tem como regra de formação o fato de um número
ser a soma dos dois anteriores, sendo que os dois primeiros termos da sequência são, respectivamente,
0 e 1. '''

n = int(input('Digite quantos termos da sequência de Fibonacci você quer ver: '))
if n != 0:
    t1 = 0
    t2 = 1
    print(f'{t1} --> {t2}', end = '')
    cont = 3
    while cont <= n:
        t3 = t1 + t2
        print(f' --> {t3}', end = '')
        t1 = t2
        t2 = t3
        cont += 1
    print('')
print('Fim do programa')