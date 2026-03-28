#from math import factorial
#fat = int(input('Digite um número para se calcular o fatorial: '))
#f = factorial(fat)
#print(f)
print('- - - CALCULADORA DE FATORIAL - - -')
print('-*' * 23)
fat = int(input('Digite um número para se calcular o fatorial: '))
print('-*' * 23)
cont = fat
f = 1 #multiplicar por 1 = o mesmo numero
while cont > 0:
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print(f)
print(f'O fatorial de {fat} é {f}')