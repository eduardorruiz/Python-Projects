""" Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em
uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3. |  C) Quais foram os números pares."""
from itertools import count
pares = ()
cont = 0
num = (int(input('Digite um número: ')), int(input('Digite mais um número: ')),
       int(input('Digite mais um número: ')), int(input('Digite um número: ')),)
print(f'Os valores digitados foram: {num}')
print(f'O número 9 foi digitado {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na posição {num.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares foram', end = ' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
