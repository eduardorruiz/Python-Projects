from random import choice
# import random
n1 = str(input('Qual o nome do primeiro aluno? '))
n2 = str(input('Qual o nome do segundo aluno? '))
n3 = str(input('Qual o nome do terceiro aluno? '))
n4 = str(input('Qual o nome do quarto aluno? '))
lista = [n1, n2, n3, n4]
print(f'Entre {n1}, {n2}, {n3} e {n4}; o aluno escolhido foi {choice(lista)}')
# print(f'Entre {n1}, {n2}, {n3} e {n4}; o aluno escolhido foi {random.choice(lista)}')