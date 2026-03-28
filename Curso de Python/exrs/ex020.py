#from random import shuffle
import random
print('O programa irá sortear em ordem aleatória 3 pessoas para uma apresentação, diga o nome dos alunos aqui a abaixo.')
nm1 = str(input('Primeiro aluno: '))
nm2 = str(input('Segundo aluno: '))
nm3 = str(input('Terceiro aluno: '))
lista = [nm1, nm2, nm3]
random.shuffle(lista)
print(f'A ordem de apresentação do trabalho será: {lista} ')
