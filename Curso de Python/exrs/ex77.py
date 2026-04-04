""" Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar
acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

tupla = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Estudar', 'Praticar', 'Trabalhar')
for n in tupla:
    print(f'\nNa palavra {n.upper()} temos as vogais', end=' ')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')