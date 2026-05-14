""" Reescreva o programa anterior lendo um número inteiro adicional chamado Prim. Nesta versão o
programa deverá apresentar os N termos da sequência de Fibonacci que forem maiores que Prim. """

# INCOMPLETO
n = int(input('Quantos termos da sequência de Fibonacci quer ver: '))
prim = int(input('Digite o número prim: '))
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